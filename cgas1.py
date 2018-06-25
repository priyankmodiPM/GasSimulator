def CGAS2(PRSH,PRSHBT,ESH,AUG,RAD,XPE,YPE,XCP,YRY,YCP,YPP,FFAR,FFAC,IZ,AMZ,INIOCC):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	DIMENSION PRSH(3,17,17),PRSHBT(3,17),ESH(3,17),AUG(3,17,17,17),RAD[3,17,17],XPE(3,17,60),YPE(3,17,60),XCP(3,54),YRY(3,54),YCP(3,54),YPP(3,54),FFAR(3,45),FFAC(3,45),IZ[3],AMZ[3],INIOCC(3,17)
	DIMENSION INIOC(17),PRBSH(17,17),ES(17),R(17,17),A[17,17,17],PRBSHBT(17)
	DIMENSION XPEK(38),YPEK(38),XPEL1(54),YPEL1(54),XPEL2(56),YPEL2(56),XPEL3(56),YPEL3(56),XPEM1(59),YPEM1(59),XPEM2(60),YPEM2(60),XPEM3(60),YPEM3(60),XENE(54),YRAY(54),YCOM(54),YPAP(54),FFR(45),FFC(45)
	# 
	# ARGON DATA FOR CASCADE CALCULATIONS
	#
	# LEVEL OCCUPANCY FOR GROUND STATE
	DATA INIOC/2,2,2,4,2,2,4,0,0,0,0,0,0,0,0,0,0/
	# AVERAGE SHAKE OFF ELECTRON ENERGY
	DATA ES/22.5,9.10,9.90,9.90,2.20,1.60,1.60,0.00,0.00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0/
	# SHAKE OFF DATA :  CARLSON AND NESTOR PHYS REV A8(1973)2887
	# % PROBABILITY OF J SHELL SHAKE OFF FROM VACANCY IN SHELL I PROBSH(I,J)
	DATA PRBSH/.001,0.30,0.54,1.07,2.47,5.86,11.45,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,.017,.056,0.11,1.66,4.18,8.33,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,.049,.043,0.17,1.73,4.41,8.71,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,.050,.080,0.13,1.73,4.37,8.72,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.16,1.37,2.82,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.25,0.57,2.33,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.25,1.12,1.74,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,170*0.0/
	# SHAKE OFF DATA : CARLSON,NESTOR ET AL PHYS REV 169(1968)27
	# % PROBABILITY OF J SHELL SHAKE OFF FROM BETA DECAY PRSHBT[J]
	DATA PRBSHBT/.264,.914,.703,1.41,4.24,5.92,11.84,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00/
	#
	# AUGER AND COSTER-KRONIG TRANSITION RATES FOR K L M AND N SHELLS 
	#  CHEN+CRASEMANN,ANDT 24(1979)13,  FOR K AND L SHELLS 
	#  MCGUIRE,SANDIA REPORTS,          FOR M AND N SHELLS 
	# K SHELL RATE (MILLIATOMIC UNITS) TO GET TO EV *0.0272105
	DATA A[1,2,2]/1.456/,A[1,2,3]/1.604/,A[1,2,4]/3.072/,A[1,2,5]/0.324/,A[1,2,6]/0.151/,A[1,2,7]/0.288/
	DATA A[1,3,3]/0.294/,A[1,3,4]/7.277/,A[1,3,5]/0.156/,A[1,3,6]/0.053/,A[1,3,7]/0.607/
	DATA A[1,4,4]/4.132/,A[1,4,5]/0.299/,A[1,4,6]/0.607/,A[1,4,7]/0.697/
	DATA A[1,5,5]/0.018/,A[1,5,6]/0.015/,A[1,5,7]/0.028/
	DATA A[1,6,7]/0.202/,A[1,7,7]/0.030/
	# L1 SHELL RATE (MILLIATOMIC UNITS)
	DATA A[2,3,5]/17.780/,A[2,3,6]/7.404/,A[2,3,7]/7.482/
	DATA A[2,4,5]/34.607/,A[2,4,6]/7.308/,A[2,4,7]/20.792/
	DATA A[2,5,5]/0.767/,A[2,5,6]/1.203/,A[2,5,7]/2.380/
	DATA A[2,6,7]/0.007/A[2,7,7]/0.068/
	# L2 AUGER SHELL RATE (MILLIATOMIC UNITS)
	# L3 AUGER SHELL RATE (MILLIATOMIC UNITS)
	DATA A[4,5,5]/0.062/,A[4,5,6]/0.041/,A[4,5,7]/1.293/
	DATA A[4,6,7]/1.719/,A[4,7,7]/2.548/
	# RADIATIVE TRANSITIONS SCOFIELD ANDT 14(1974)121
	# DIPOLE AND HIGHER MULTIPOLES , RELATIVISTIC CALC. UNITS 1.519E15/SEC
	# K-SHELL
	DATA R(1,2)/2.34E-9/,R(1,3)/.02226/,R(1,4)/.044/,R(1,5)/3.36E-10/,R(1,6)/1.822E-3/,R(1,7)/3.60E-3/
	# L1 SHELL
	DATA R(2,3)/8.75E-6/,R(2,4)/1.97E-5/,R(2,5)/7.22E-14/,R(2,6)/7.18E-5/,R(2,7)/1.378E-4/
	# L2 SHELL
	DATA R(3,4)/7.88E-14/,R(3,5)/2.43E-5/,R(3,6)/1.21E-14/,R(3,7)/1.05E-8/
	# L3 SHELL
	DATA R(4,5)/2.48E-5/,R(4,6)/5.29E-9/,R(4,7)/5.19E-9/
	# RADIATIVE TRANSITIONS MANSON AND KENNEDY ANDT 14(1974)111
	# DIPOLE ONLY NON-RELATIVISTIC CALC.  UNITS   1/SEC
	# M1 SHELL
	DATA R(5,6)/2.0708E9/,R(5,7)/4.1416E9/
	# 
	# PHOTOELECTRIC ABSORPTION X-SECTIONS FOR EACH SHELL: 
	#    UNITS BARNS/ATOM AND ENERGIES IN EV
	#  ASSEMBLED FROM: BAND ET AL.            ANDT 23(1979)443
	#                : KENNEDY AND MANSON     PHYS REV A5(1972)227
	#                : SCOFIELD               UCRL-51326
	#                : SAMSON AND STOLTE      J.ELEC.SPEC. 123(2002)265
	#                : CHAN ET AL             PHYS REV A46(1992)149
	#                : MARR AND WEST          ANDT 18(1976)497
	#                : VIEGELE                ATOMIC DATA 5(1973)50
	# KSHELL 1S 1/2
	DATA YPEK/7.53E4,4.51E4,2.53E4,1.55E4,7.06E3,3.77E3,1.17E3,498.,146.,60.2,30.0,17.0,6.85,3.38,.938,.382,.111,.0485,.0264,.0165,.00839,.00522,.00244,.00152,8.31E-4,5.64E-4,4.24E-4,3.39E-4,2.41E-4,1.87E-4,1.19E-4,8.75E-5,5.70E-5,4.23E-5,3.36E-5,2.79E-5,2.08E-5,1.66E-5/
	DATA XPEK/3205.9,4000.,5000.,6000.,8000.,1.0E4,1.5E4,2.0E4,3.0E4,4.0E4,5.0E4,6.0E4,8.0E4,1.0E5,1.5E5,2.0E5,3.0E5,4.0E5,5.0E5,6.0E5,8.0E5,1.0E6,1.5E6,2.0E6,3.0E6,4.0E6,5.0E6,6.0E6,8.0E6,1.0E7,1.5E7,2.0E7,3.0E7,4.0E7,5.0E7,6.0E7,8.0E7,1.0E8/
	# L1 SHELL 2S 1/2
	DATA YPEL1/3.20E5,3.38E5,3.35E5,3.26E5,3.15E5,2.92E5,2.72E5,2.62E5,1.77E5,1.19E5,9.46E4,8.06E4,6.79E4,5.89E4,2.64E4,1.43E4,5.71E3,2.86E3,1.64E3,1.03E3,483.,264.,84.9,37.0,11.1,4.66,2.35,1.34,.544,.270,.0755,.0308,.00903,.00394,.00215,.00135,6.83E-4,4.25E-4,1.99E-4,1.24E-4,6.78E-5,4.60E-5,3.46E-5,2.77E-5,1.97E-5,1.52E-5,9.73E-6,7.14E-6,4.65E-6,3.45E-6,2.74E-6,2.27E-6,1.69E-6,1.35E-6/
	DATA XPEL1/326.3,333.1,339.9,346.7,353.5,367.1,380.7,392.,525.,676.5,775.,849.,932.,1000.,1500.,2000.,3000.,4000.,5000.,6000.,8000.,1.0E4,1.5E4,2.0E4,3.0E4,4.0E4,5.0E4,6.0E4,8.0E4,1.0E5,1.5E5,2.0E5,3.0E5,4.0E5,5.0E5,6.0E5,8.0E5,1.0E6,1.5E6,2.0E6,3.0E6,4.0E6,5.0E6,6.0E6,8.0E6,1.0E7,1.5E7,2.0E7,3.0E7,4.0E7,5.0E7,6.0E7,8.0E7,1.0E8/
	# L2 SHELL 2P 1/2
	DATA YPEL2/1.80E6,1.31E6,9.57E5,8.67E5,8.37E5,8.17E5,7.80E5,6.87E5,6.10E5,5.40E5,2.65E5,1.36E5,9.40E4,7.28E4,5.60E4,4.56E4,1.37E4,5.61E3,1.51E3,577.,268.,142.,50.7,22.5,5.00,1.68,.354,.116,.0488,.0241,.00793,.00338,7.46E-4,2.63E-4,6.51E-5,2.57E-5,1.31E-5,7.72E-6,3.59E-6,2.08E-6,8.63E-7,5.36E-7,2.94E-7,2.00E-7,1.50E-7,1.20E-7,8.54E-8,6.61E-8,4.22E-8,3.09E-8,2.02E-8,1.50E-8,1.19E-8,9.86E-9,7.35E-9,5.86E-9/
	DATA XPEL2/250.6,257.4,264.2,271.0,277.8,291.4,305.0,332.2,359.4,386.6,525.,676.5,775.,849.,932.,1000.,1500.,2000.,3000.,4000.,5000.,6000.,8000.,1.0E4,1.5E4,2.0E4,3.0E4,4.0E4,5.0E4,6.0E4,8.0E4,1.0E5,1.5E5,2.0E5,3.0E5,4.0E5,5.0E5,6.0E5,8.0E5,1.0E6,1.5E6,2.0E6,3.0E6,4.0E6,5.0E6,6.0E6,8.0E6,1.0E7,1.5E7,2.0E7,3.0E7,4.0E7,5.0E7,6.0E7,8.0E7,1.0E8/
	# L3 SHELL 2P 3/2
	DATA YPEL3/3.60E6,2.63E6,1.91E6,1.73E6,1.67E6,1.63E6,1.56E6,1.37E6,1.22E6,1.08E6,5.21E5,2.67E5,1.84E5,1.43E5,1.09E5,8.93E4,2.67E4,1.09E4,2.93E3,1.11E3,514.,271.,96.4,42.6,9.36,3.12,.647,.209,.0869,.0424,.0137,.00575,.00122,4.23E-4,1.03E-4,4.07E-5,2.10E-5,1.27E-5,6.22E-6,3.79E-6,1.72E-6,1.07E-6,5.86E-7,3.98E-7,2.99E-7,2.39E-7,1.70E-7,1.32E-7,8.41E-8,6.17E-8,4.02E-8,2.98E-8,2.37E-8,1.96E-8,1.46E-8,1.17E-8/
	DATA XPEL3/248.4,255.2,262.0,268.8,275.6,289.2,302.8,330.0,357.2,384.4,525.,676.5,775.,849.,932.,1000.,1500.,2000.,3000.,4000.,5000.,6000.,8000.,1.0E4,1.5E4,2.0E4,3.0E4,4.0E4,5.0E4,6.0E4,8.0E4,1.0E5,1.5E5,2.0E5,3.0E5,4.0E5,5.0E5,6.0E5,8.0E5,1.0E6,1.5E6,2.0E6,3.0E6,4.0E6,5.0E6,6.0E6,8.0E6,1.0E7,1.5E7,2.0E7,3.0E7,4.0E7,5.0E7,6.0E7,8.0E7,1.0E8/
	# M1 SHELL 3S 1/2
	DATA YPEM1/5.6E4,1.87E5,2.62E5,3.07E5,3.27E5,3.27E5,3.07E5,2.54E5,2.08E5,1.79E5,1.36E5,7.16E4,4.04E4,2.39E4,1.49E4,1.15E4,9.67E3,8.05E3,7.00E3,3.04E3,1.62E3,639.,320.,183.,115.,54.1,29.6,9.53,4.17,1.26,.527,.266,.151,.0616,.0306,.00856,.00350,.00102,4.47E-4,2.44E-4,1.53E-4,7.75E-5,4.82E-5,2.26E-5,1.40E-5,7.70E-6,5.23E-6,3.93E-6,3.14E-6,2.24E-6,1.73E-6,1.10E-6,8.10E-7,5.28E-7,3.92E-7,3.11E-7,2.58E-7,1.92E-7,1.53E-8/
	DATA XPEM1/29.239,36.0,42.8,49.6,56.4,70.0,83.6,110.8,138.0,151.4,184.,278.,392.,525.,676.5,775.,849.,932.,1000.,1500.,2000.,3000.,4000.,5000.,6000.,8000.,1.0E4,1.5E4,2.0E4,3.0E4,4.0E4,5.0E4,6.0E4,8.0E4,1.0E5,1.5E5,2.0E5,3.0E5,4.0E5,5.0E5,6.0E5,8.0E5,1.0E6,1.5E6,2.0E6,3.0E6,4.0E6,5.0E6,6.0E6,8.0E6,1.0E7,1.5E7,2.0E7,3.0E7,4.0E7,5.0E7,6.0E7,8.0E7,1.0E8/
	# M2 SHELL 3P 1/2
	DATA YPEM2/10.3E6,11.9E6,11.3E6,7.23E6,3.33E6,8.83E5,2.43E5,1.67E5,2.25E5,2.81E5,3.24E5,3.58E5,3.77E5,3.80E5,3.79E5,3.69E5,3.45E5,3.25E5,2.97E5,2.80E5,2.38E5,2.00E5,1.67E5,1.40E5,1.09E5,7.40E4,3.58E4,1.81E4,9.65E3,6.82E3,5.37E3,4.19E3,3.44E3,1.09E3,458.,127.,49.4,23.3,12.4,4.49,2.01,.450,.152,.0322,.0106,.00446,.00221,7.29E-4,3.11E-4,6.85E-5,2.42E-5,5.98E-6,2.36E-6,1.20E-6,7.07E-7,3.27E-7,1.89E-7,7.82E-8,4.86E-8,5.31E-10/
	DATA XPEM2/15.937,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,100.,110.,120.,130.,150.,170.,190.,210.,245.,278.,392.,525.,676.5,775.,849.,932.,1000.,1500.,2000.,3000.,4000.,5000.,6000.,8000.,1.0E4,1.5E4,2.0E4,3.0E4,4.0E4,5.0E4,6.0E4,8.0E4,1.0E5,1.5E5,2.0E5,3.0E5,4.0E5,5.0E5,6.0E5,8.0E5,1.0E6,1.5E6,2.0E6,1.0E8/
	# M3 SHELL 3P 3/2
	DATA YPEM3/20.5E6,23.8E6,22.5E6,14.5E6,6.67E6,1.77E6,4.87E5,3.33E5,4.50E5,5.62E5,6.49E5,7.15E5,7.53E5,7.60E5,7.57E5,7.37E5,6.89E5,6.51E5,5.95E5,5.60E5,4.76E5,4.00E5,3.33E5,2.80E5,2.17E5,1.47E5,7.06E4,3.55E4,1.89E4,1.34E4,1.05E4,8.19E3,6.73E3,2.12E3,889.,246.,95.1,44.6,23.7,8.50,3.78,.839,.281,.0587,.0190,.00792,.00387,.00125,5.26E-4,1.12E-4,3.88E-5,9.43E-6,3.75E-6,1.94E-6,1.17E-6,5.75E-7,3.51E-7,1.62E-7,1.01E-7,1.10E-9/
	DATA XPEM3/15.760,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,100.,110.,120.,130.,150.,170.,190.,210.,245.,278.,392.,525.,676.5,775.,849.,932.,1000.,1500.,2000.,3000.,4000.,5000.,6000.,8000.,1.0E4,1.5E4,2.0E4,3.0E4,4.0E4,5.0E4,6.0E4,8.0E4,1.0E5,1.5E5,2.0E5,3.0E5,4.0E5,5.0E5,6.0E5,8.0E5,1.0E6,1.5E6,2.0E6,1.0E8/
	#  RAYLEIGH, COMPTON AND PAIR PR0DUCTION 
	# HUBBEL J.PHYS.CHEM.REF.DATA 4(1975)471
	# HUBBEL  NIST XCOM WEB SITE
	# STORM AND ISRAEL NUCL.DATA TABLES A7(1970)565
	DATA XENE/100.,150.,200.,300.,400.,500.,600.,800.,1000.,1500.,2000.,3000.,4000.,5000.,6000.,8000.,1.0D4,1.5D4,2.0'%.3f' %.0D4,4.0D4,5.0D4,6.0D4,8.0D4,1.0D5,1.5D5,2.0'%.3f' %.0D5,4.0D5,5.0D5,6.0D5,8.0D5,1.0D6,1.022D6,1.25D6,1.5D6,2.0D6,2.044'%.3f' %.0D6,4.0D6,5.0D6,6.0D6,7.0D6,8.0D6,9.0D6,1.0D7,1.5D7,2.0'%.3f' %.0D7,4.0D7,5.0D7,6.0D7,8.0D7,1.0D8/
	DATA YRAY/215.5,215.2,215.0,214.2,213.2,211.9,210.3,206.5,201.7,187.2,170.5,138.2,112.4,93.45,79.70,61.33,49.16,30.22,20.01,10.72,      6.776,4.690,3.435,2.061,1.369,.6390,.3681,.1671,.09475,.06089,    .04238,.02389,.01531,.01466,9.804D-3,6.811D-3,3.833D-3,3.669D-3,1.704D-3,9.585D-4,         6.135D-4,4.260D-4,3.130D-4,2.397D-4,1.894D-4,1.534D-4,6.788D-5,3.818D-5,1.697D-5,9.545D-6,6.109D-6,4.242D-6,2.386D-6,1.527D-6/  
	DATA YCOM/5.185D-3,.01168,.02080,.04655,.08210,.1270,.1806,.3117,.4696,.9421,                        1.462,2.466,3.332,4.046,4.624,5.501,6.161,7.330,8.048,8.727,8.961,9.013,8.975,8.767,8.493,7.800,7.209,6.314,5.674,5.189,4.805,4.225,3.801,3.761,3.400,3.090,2.638,2.605,2.076,1.731,1.495,1.322,1.188,1.081,.9938,.9208,.6815,.5470,.3982,.3164,    .2641,.2276,.1795,.1490/      
	# TOTAL PAIR PRODUCTION NUCLEAR + ELECTRON
	DATA YPAP/34*1.D-20,2.826D-3,.01507,.05880,.06336,.1665,.2700,    .3627,.4462,.5208,.5882,.6493,.7049,.9170,1.072,1.296,1.446,      1.563,1.650,1.779,1.876/   
	# NORMALISED RAYLEIGH FORM FACTOR  Hubbel
	DATA FFR/1.0,.99967,.99889,.99761,.99578,.99339,.99056,.98333,.9744,.9506,  .9217,.9050,.8606,.8078,.7656,.7189,.6350,.5667,.4746,.4202,.3814,.3465,.3122,.2787,.2468,.1796,.1343,.08906,.07183,.06278,.05371,.04672,.03272,.02292,.01596,.0126,.005872,.001555,5.553D-4,1.744D-5,2.907D-6,1.250D-6,3.693D-10,2.99D-19,3.37D-28/  
	DATA FFC/5.6D-22,3.33D-4,.00133,.003011,.005328,.008283,.01185,.02073,.03172,.05906,  .09133,.1087,.1533,.1977,.2400,.2796,.3502,.4098,.4999,.5617,.6094,.6517,.6900,.7256,.7572,.8189,.8606,.9067,.9328,.9517,.9661,.9761,.9889,.9950,.99756,.99878,.99967,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0/
	# ARGON ATOMIC NUMBER
	IZ[1]=18
	AMZ[1]=39.948
	# CONVERT SHAKE OFF FROM A % TO A PROBABILITY
	DO 1 I=1,17
	PRSHBT(1,I)=PRBSHBT[I]/100.0
	DO 1 J=1,17
	PRBSH(I,J)=PRBSH(I,J)/100.0
	1 CONTINUE  
	# SWAP INDICES AND DO CHECK SUM
	DO 2 I=1,17
	PRSUM=0
	DO 2 J=1,17
	PRSH(1,I,J)=PRBSH[J][I]
	#     PRSUM=PRSUM+PRSH(I,J)
	#     WRITE(6,888) I,PRSUM
	# 888 print(' I=',I3,' PRSUM=','%.3f' %)
	2 CONTINUE
	# LOAD SKAKE OFF ENERGIES AND LEVEL OCCUPATIONS
	DO 3 I=1,17
	ESH(1,I)=ES[I]
	INIOCC(1,I)=INIOC[I]
	3 CONTINUE
	#
	# AUGER PROBABILITIES IN ARRAY AUG(I,J,K) INITIAL VACANCY IN SHELL I,
	# WITH TRANSITION TO SHELLS J,K
	# LOAD OUTPUT ARRAYS AND CONVERT TO EV
	DO 4 I=1,4
	DO 4 J=1,17
	DO 4 K=1,17 
	4 AUG(1,I,J,K)=A[I,J,K]*0.0272105  
	DO 5 I=5,17
	DO 5 J=1,17
	DO 5 K=1,17
	5 AUG(1,I,J,K)=A[I,J,K]*0.00272105
	# CHECK AUGER LEVEL SUMS
	#     DO 7 I=1,17
	#     ASUM=0.0
	#     DO 6 J=1,17
	#     DO 6 K=1,17
	#   6 ASUM=ASUM+AUG(I,J,K)
	#     WRITE(6,887) I,ASUM
	# 887 print(' I=',I3,' ASUM=','%.3f' %)
	#   7 CONTINUE
	#  
	# CONVERT RADIATIVE RATES IN M AND N SHELL TO EV 
	DO 12 I=5,17
	DO 12 J=6,17
	12 R(I,J)=R(I,J)*6.582119D-16
	# LOAD OUTPUT ARRAY
	DO 13 I=1,17
	DO 13 J=1,17
	13 RAD[1,I,J]=R(I,J)
	# PRINTOUT CHECK SUM
	#     DO 15 I=1,17
	#     RSUM=0.0
	#     DO 14 J=1,17
	#  14 RSUM=RSUM+R(I,J)
	#     WRITE(6,100) I,RSUM
	# 100 print(' SHELL =',I3,' RAD RATE EV=','%.3f' %)
	#  15 CONTINUE
	# LOAD PHOTOELECTRIC DATA
	DO 21 J=1,38
	XPE(1,1,J)=math.log(XPEK[J])
	YPE(1,1,J)=math.log(YPEK[J]*1.D-24)
	21 CONTINUE
	DO 22 J=1,54
	XPE(1,2,J)=math.log(XPEL1[J])
	YPE(1,2,J)=math.log(YPEL1[J]*1.D-24)
	22 CONTINUE 
	DO 23 J=1,55
	XPE(1,3,J)=math.log(XPEL2[J])
	YPE(1,3,J)=math.log(YPEL2[J]*1.D-24)
	23 CONTINUE 
	DO 24 J=1,55
	XPE(1,4,J)=math.log(XPEL3[J])
	YPE(1,4,J)=math.log(YPEL3[J]*1.D-24)
	24 CONTINUE 
	DO 25 J=1,59
	XPE(1,5,J)=math.log(XPEM1[J])
	YPE(1,5,J)=math.log(YPEM1[J]*1.D-24)
	25 CONTINUE 
	DO 26 J=1,60
	XPE(1,6,J)=math.log(XPEM2[J])
	YPE(1,6,J)=math.log(YPEM2[J]*1.D-24)
	26 CONTINUE 
	DO 27 J=1,60
	XPE(1,7,J)=math.log(XPEM3[J])
	YPE(1,7,J)=math.log(YPEM3[J]*1.D-24)
	27 CONTINUE 
	# LOAD RAYLEIGH COMPTON AND PAIR PRODUCTION DATA
	DO 28 J=1,54
	XCP[1][J]=math.log(XENE[J])
	YRY[1][J]=math.log(YRAY[J]*1.D-24)
	YCP[1][J]=math.log(YCOM[J]*1.D-24)
	YPP[1][J]=math.log(YPAP[J]*1.D-24)
	28 CONTINUE
	# LOAD RAYLEIGH AND COMPTON FORM FACTORS
	DO 29 J=1,45
	FFAR[1][J]=FFR[J]
	FFAC[1][J]=FFC[J]
	29 CONTINUE
	return 
	# end