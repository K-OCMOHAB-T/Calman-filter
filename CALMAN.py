import random
import math

pi2 = 6.283185307179586
pi = 3.1415926535897932

def Normalrand(rand01, sigma):
    saverand=rand01
    while 1:
        stimerand=saverand
        saverand=random.random()
        error=sin(pi2*stimerand)*sqrt(2.0*log(1.0/saverand))
        if fabs(error)<sigma:
			           break
    return error

MOD=1
sigmaobs=100.0
sigmamod=1.0

if MOD:
	randerr=1.0
	random.seed(888)
    x=0.0
	h=0.001
	obs=open('obs.txt' ,'w')
	
	while 1:
		rand01=random.random()*randerr
		z=sin(x)+Normalrand(rand01, sigmaobs)
		obs.write(x, "\t", z, "\n")
		x+=h 
		if x>pi2: 
			break
	obs.close()

obs=open('obs.txt' ,'r')
out=open('result.txt' ,'w')
	
sigmaobs2=sigmaobs*sigmaobs
sigmamod2=sigmamod*sigmamod
E=sigmaobs2
K=1.0
while 1:
	mem=K;
	E=sigmaobs2*(E+sigmamod2)/(E+sigmaobs2+sigmamod2);
	K=E/sigmaobs2;
	if (sqrt((K-mem)*(K-mem))<0.0000001):
		break
	
line = obs.readline()
stroka = line.split('\t') 
x=float(stroka[0])
z=float(stroka[1])

mem=x
x0=sin(x)
out.write( x,"\t",x0,"\t",z,"\n")

while 1:
	line = obs.readline()
	stroka = line.split('\t') 
	x=float(stroka[0])
	z=float(stroka[1])
	x0=K*z+(1.0-K)*x0
	mem=x
	out.write( x,"\t",x0,"\t",z,"\n") 	
	
obs.close()
out.close()