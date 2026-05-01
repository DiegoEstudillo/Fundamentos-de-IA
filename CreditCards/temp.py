import pandas as pd
import webbrowser
datos = pd.read_csv("csv_camaras.csv")
df = pd.DataFrame(datos)
script = ""
i=0
while i<11:
        script = script+"{x:'"+datos['Model'].loc[i]+"', y:"+str(datos['Price'].loc[i])+", z:"+str(i+1)+"},\n"
        i+=1
print (script)
#df.groupby('Name')['Transaction'].sum().plot(kind='line',legend='Reverse',title='Transacciones',color='gray')
df.groupby('Model')['Price'].sum().plot(kind='bar',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='barh',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='hist',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='box',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='kde',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='density',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='area',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='pie',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='scatter',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='hexbin',legend='Reverse')
f = open('camaras.html','w')

mensaje = """<html>
<head>
<title>Gráficas con JavaScript</title>
<meta charset='utf-8'>
<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>
<link rel='stylesheet' type='text/css' href='morris.css'>  
<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js'></script>
<script src='http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js'></script>
<script src='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js' integrity='sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM' crossorigin='anonymous'></script> 
<script src='morris.min.js'></script>
<script>    
function grafica1(){
  new Morris.Bar({
  element: 'graph',
  data: ["""+script+"""
          ],
  xkey: 'x',
  ykeys: ['y'],
  axes:false,
  labels: ['Cantidad:'],
  resize:true,
  lineColors:['#2CB4AC']
  });
}
</script>
</head>
<body>
<div id='graph'></div>
<input type='button' value='grafica' onclick='grafica1()'>
</body>
</html>"""
f.write(mensaje)
f.close()

webbrowser.open_new_tab('CreditCards.html')

#print(datos.to_excel("CreditCards.xls",sheet_name="datos"))