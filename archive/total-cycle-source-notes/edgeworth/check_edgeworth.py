#!/usr/bin/env python3
"""Exact algebra and numerical consistency checks for total-cycle Edgeworth transfer.

The tests do not verify the upstream Luce switching theorem or prove asymptotics.
Run: python check_edgeworth.py --output edgeworth_checks.json
Requires Python 3, numpy, scipy, and sympy.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.special import ndtr
from scipy.stats import poisson


def phi(x: np.ndarray) -> np.ndarray:
    return np.exp(-x*x/2)/math.sqrt(2*math.pi)


def first(x: np.ndarray, mu: float, fraction: float) -> np.ndarray:
    return ndtr(x)+phi(x)/math.sqrt(mu)*(0.5-fraction+(1-x*x)/6)


def second_mid(k: np.ndarray, mu: float, c2: float = 0.0) -> np.ndarray:
    y=(k+0.5-mu)/math.sqrt(mu)
    return (ndtr(y)+phi(y)*(1-y*y)/(6*math.sqrt(mu))
            +phi(y)/mu*((-y**5+7*y**3-3*y)/72-c2*y/2))


def taylor_checks() -> int:
    w=sp.Symbol('w')
    count=0
    for order in range(1,6):
        for m in range(0,25):
            base=sum(sp.binomial(m,j)*w**j for j in range(order+1))
            rem=sum(sp.binomial(m-1-j,order)*(1+w)**j*w**(order+1)
                    for j in range(max(0,m-order)))
            assert sp.expand((1+w)**m-base-rem)==0, (order,m)
            count+=1
    return count


def charlier_checks() -> int:
    z,lam=sp.symbols('z lam', positive=True)
    count=0
    for j in range(1,7):
        c=sum((-1)**(j-r)*sp.binomial(j,r)*sp.ff(z,r)*lam**(j-r)
              for r in range(j+1))
        poly=sp.Poly(sp.expand(c*c),z)
        expectation=sum(coef*sp.bell(power[0],lam) for power,coef in poly.terms())
        assert sp.expand(expectation-sp.factorial(j)*lam**j)==0,j
        count+=1
    return count


def poisson_tests() -> list[dict]:
    rows=[]
    fractions=(0.0,0.125,0.5,0.875,1.0-2**-30)
    for mu in (8.25,20.,50.5,100.,300.25,1000.,3000.5,10000.):
        lo=max(-2,int(math.floor(mu-12*math.sqrt(mu))))
        hi=int(math.ceil(mu+12*math.sqrt(mu)))
        k=np.arange(lo,hi+1,dtype=float)
        cdf=poisson.cdf(k,mu)
        e1=0.
        for f in fractions:
            x=(k+f-mu)/math.sqrt(mu)
            e1=max(e1,float(np.max(np.abs(cdf-first(x,mu,f)))))
        e2=float(np.max(np.abs(cdf-second_mid(k,mu))))
        assert e1*mu<1.0,(mu,e1)
        assert e2*mu**1.5<1.0,(mu,e2)
        # A right-continuous integer threshold close to the mean realizes the
        # predicted leading Kolmogorov constant asymptotically.
        kk=int(round(mu))
        at_right=math.sqrt(mu)*(poisson.cdf(kk,mu)-ndtr((kk-mu)/math.sqrt(mu)))
        rows.append(dict(mu=mu,thresholds=len(k),phase_values=len(fractions),
                         first_max_error=e1,mu_times_first_error=e1*mu,
                         second_max_error=e2,mu_3_over_2_times_second_error=e2*mu**1.5,
                         scaled_right_jump_error=float(at_right)))
    return rows


def convolution_tests() -> list[dict]:
    rows=[]
    for lam in (10.,30.,100.,300.,1000.,3000.):
        m=max(1,int(math.log(lam)))
        marks=[('zero',np.array([1.])),
               ('Bernoulli',np.array([.65,.35])),
               ('deterministic',np.eye(1,m+1,m)[0]),
               ('two_point',np.r_[.7,np.zeros(2*m-1),.3]),
               ('binomial',np.array([math.comb(m,j)*.4**j*.6**(m-j)
                                     for j in range(m+1)]))]
        for name,pm in marks:
            j=np.arange(len(pm),dtype=float)
            nu=float(np.dot(j,pm))
            fact2=float(np.dot(j*(j-1),pm))
            fact3=float(np.dot(j*(j-1)*(j-2),pm))
            c2=fact2-nu*nu
            mu=lam+nu
            top=int(math.ceil(mu+16*math.sqrt(mu)+4*len(pm)+20))
            k=np.arange(top+1,dtype=float)
            p=poisson.pmf(k,lam)
            actual=np.convolve(p,pm)[:top+1]
            ref=poisson.pmf(k,mu)
            delta2=np.r_[0.,0.,ref[:-2]]-2*np.r_[0.,ref[:-1]]+ref
            signed=ref+(c2/2)*delta2
            tv=.5*float(np.abs(actual-signed).sum())
            bound=math.sqrt(6)/(2*lam**1.5)*((fact3+nu**3)/6+abs(c2)*nu/2)
            assert tv<=bound+2e-11,(lam,name,tv,bound)
            cdf=np.cumsum(actual)
            e2=float(np.max(np.abs(cdf-second_mid(k,mu,c2))))
            rows.append(dict(lambda_core=lam,mark=name,mu=mu,c2=c2,
                             signed_half_l1=tv,proved_smoothing_bound=bound,
                             second_cdf_error=e2))
    return rows


def uniform_permutation_tests() -> list[dict]:
    ns=(100,1000,10000,100000)
    p=np.zeros(180); p[0]=1.
    h1=h2=0.
    rows=[]
    for n in range(1,max(ns)+1):
        q=1/n
        p[1:]=(1-q)*p[1:]+q*p[:-1]
        p[0]*=(1-q)
        h1+=q; h2+=q*q
        if n in ns:
            k=np.arange(len(p),dtype=float)
            err=float(np.max(np.abs(np.cumsum(p)-second_mid(k,h1,-h2))))
            wrong=float(np.max(np.abs(np.cumsum(p)-second_mid(k,h1,0.))))
            assert abs(float(p.sum())-1)<2e-10
            rows.append(dict(n=n,mu=h1,c2=-h2,
                             second_error=err,poisson_second_error=wrong,
                             scaled_second_error=err*h1**1.5))
    return rows


def polynomial_checks() -> dict:
    y=sp.Symbol('y')
    H3=y**3-3*y;H5=y**5-10*y**3+15*y
    q=sp.expand(-H3/24-H5/72+y/24)
    assert sp.expand(q-(-y**5+7*y**3-3*y)/72)==0
    # For x>=0, the supremum over lattice phase has factor
    # exp(-x^2/2)*(1/2+|1-x^2|/6). On [0,1] and [1,infinity)
    # its derivative is respectively x(x^2-6)/6 and -x^3/6.
    x=sp.Symbol('x',real=True)
    d1=sp.simplify(sp.diff(sp.exp(-x*x/2)*(4-x*x)/6,x)/sp.exp(-x*x/2))
    d2=sp.simplify(sp.diff(sp.exp(-x*x/2)*(x*x+2)/6,x)/sp.exp(-x*x/2))
    assert sp.expand(d1-x*(x*x-6)/6)==0
    assert sp.expand(d2+x**3/6)==0
    return dict(midpoint_polynomial=str(q),kolmogorov_constant=2/(3*math.sqrt(2*math.pi)))


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=Path('edgeworth_checks.json'))
    args=ap.parse_args()
    result=dict(exact_taylor_cases=taylor_checks(),
                exact_charlier_norm_identities=charlier_checks(),
                polynomial_checks=polynomial_checks(),
                poisson_cdf_tests=poisson_tests(),
                convolution_tests=convolution_tests(),
                uniform_permutation_tests=uniform_permutation_tests(),
                status='All checks passed',
                limitations='Finite algebra and numerical consistency checks only; not a proof of upstream switching or asymptotics.')
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('poisson_cdf_tests','convolution_tests','uniform_permutation_tests')},indent=2))
    print('Poisson test rows:',len(result['poisson_cdf_tests']))
    print('Convolution test rows:',len(result['convolution_tests']))
    print('Uniform-permutation rows:',len(result['uniform_permutation_tests']))

if __name__=='__main__':
    main()
