# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 08:21:23 2017

@author: Ricardo
"""


def binomial():      
        n=int(input('Ingrese numero de elementos  '))
        k=int(input('Ingrese numero de conjuntos que desea  '))
        a=[]
        # a continuación se inicializa una matriz con ceros
        for i in range(0,n+1):
            a.append([0]*(k+1))

            # A continuación se llena la matriz con valores ingresados
        if n==k or k==0:
           print'el arreglo binomial es  ',1 
        else:
            for i in range(0,n+1):
                a[i][0]=1
    
            for i in range(1,n+1):
                a[i][1]=i
    
            for i in range(2,k+1):
                a[i][i]=1
            #for i in range(2,k+1):
                #a[i][i]=1
            for i in range(3,n+1):
                for j in range(2,i-1):
                    if j<=k:
                        a[i][j]=a[i-1][j-1]+a[i-1][j]                   
            print'el arreglo binomial es  ',a[n][k]
            print'la matriz generada es   ',a
binomial()