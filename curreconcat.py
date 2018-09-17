## for the list


curr = ['EURUSD' , 'EURNOK' , 'EURMXN' , 'EURSGD' , 'USDSGD' , 'EURAUD' , 'EURGBP' , 'EURAED' , 'EURDOP' , 'EURPLN' , 'EURCAD' , 'USDDOP' , 'EURCNY' , 'USDMXN' , 'EURSEK' , 'EURXOF' , 'EURRUB' , 'EURCZK' , 'EURMAD' , 'EURCHF' , 'USDCAD' , 'USDAED' , 'GBPUSD' , 'GBPMXN' , 'EURTND' , 'EURDKK' , 'EURIDR' , 'EURHKD' , 'AUDUSD' , 'EURZAR' , 'USDCNY' , 'USDHKD' , 'USDIDR' , 'EURBRL' , 'EURJPY' , 'EURTHB' , 'GBPTRY' , 'EURTRY' , 'USDTRY' , 'USDBRL' , 'USDTHB' , 'GBPCAD' , 'GBPSEK' , 'EURMYR' , 'GBPAED' , 'USDSEK' , 'USDDKK']
month = ['10','11','12','01','02','03','04','05','06','07','08']

for m in month:
	for c in curr:
		print(m+c)






## for CONCAT


for n in range(48):
	print(f'A{n}, \"\' , \'\", ', end='')