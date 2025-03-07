# LAB 3- Fiesta de coctel.
## Descripcion:
Este proyecto abarca el código necesario para hacer el respectivo análisis detallado de señales de audio en un entorno con diversas fuentes sonoras, ejecutando el conocido problema de la fiesta de coctel, para esto se emplean diferentes técnicas de procesamiento digital de señales en Python, como por ejemplo la relación señal-ruido (SNR), la transformada rápida de Fourier (FFT) y la transformada de Fourier de tiempo corto (STFT) para hacer un análisis espectral. También, se hace el análisis de componentes independientes (ICA) para separar las fuentes, permitiendo aislar la voz deseada de las tres señales mezcladas capturadas por tres micrófonos de los celulares por medio de la aplicación grabadora de voz que ya viene con el sistema operativo de cada dispositivo. Gracias a estas técnicas se estudia la influencia del ruido y la distribución espacial de los micrófonos, logrando una mejor comprensión del problema y su resolución en aplicaciones biomédicas o en este caso caracterizar la voz de un personaje especifico. 


Cabe resaltar que estos audios se grabaron en el salón de danza de la UMNG ubicando los tres dispositivos celulares en el centro del salón en el suelo, cada uno ubicado con el micrófono en una posición distinta para así poder tomar el sonido desde diferentes ángulos, cada uno de nosotros también nos ubicamos a diferentes distancias, por ejemplo, Melany se hizo a aproximadamente 2 metros en diagonal a un micrófono, Santiago se hizo aproximadamente a 3,5 metros en diagonal a un micrófono y Mariajosé a 3 metros en diagonal al otro micrófono, lo que hace similar a los tres audios es que los primeros 5 segundos de grabación se toman como el ruido y luego cada uno de nosotros empieza a hablar al mismo tiempo por aproximadamente 36 segundos. 

## Instrucciones y estructura del codigo
Se hará una breve explicación de las partes importantes del código para su mayor entendimiento. 
![image](https://github.com/user-attachments/assets/9a208adf-255d-4e2a-a89c-85d12efa2e48)





*Importación de librerías.*


La librería numpy sirve para realizar operaciones matemáticas, librosa para cargar y procesar señales de audio, matplotlib.pyplot para graficar las señales y sus espectros, soundfile para guardar los archivos de audio procesados, scipy.fftpack y scipy signal para calcular FFT y análisis espectral, sklearn.decomposition.FastICA para separar las fuentes de audio o aislar la voz y os se usa para lograr abrir y reproducir el archivo de audio guardado ya previamente aislado. 

![image](https://github.com/user-attachments/assets/655cb564-e4b6-4f78-8ee1-e34d9a403b9c)





*Funcion para calcular el ruido.*





Se usa para evaluar la calidad de la separación de la voz midiendo la relación entre la potencia de la señal y la del ruido. 



![image](https://github.com/user-attachments/assets/1580c947-68dc-4176-89eb-3e181fdf9aef)








*Carga y procesamiento de audios.*







Carga 3 archivo de audio tipo .wav en una lista y los convierte a una frecuencia de muestre fija, valor de 16 KHz para así poder asegurar que todas logren tener la misma resolución temporal y luego esta se almacena en una lista signals.


![image](https://github.com/user-attachments/assets/3946aecd-1503-4a0e-a633-b9744fe73c70)







*Ajustar la longitud de las señales.*






La función de esta parte es encontrar la señal más larga y rellenar con ceros gracias a la función np.pad las señales más cortas para que así todas puedan tener la misma longitud y facilitar el trabajo y disminuir los errores. 

![image](https://github.com/user-attachments/assets/de9ab965-865e-4cb1-a0aa-e1a5f5e0a2eb)








*Extraccion de los 5 segundos de ruido.*








Se extraen los primeros 5 segundo sde audio de cada señal que serán la referencia del ruido.




![image](https://github.com/user-attachments/assets/8e983ffc-13fa-47b1-9377-e82c13db4695)







*Calculo SNR para cada señal.*



Cumple la función de calcular el SNR de cada señal con respecto a su ruido dando uso de la función calculate_snr y así luego poder imprimir los valores en la consola. 





![image](https://github.com/user-attachments/assets/0d90e908-9cf7-425c-87aa-42fa966cd131)





*Generación de gráficas.*


Lo que hace esta parte es que mostrara tres gráficos por cada uno de los audios subidos (9 graficos en total) cada señal tiene gráfico de forma de la onda, su transformada rápida de Fourier (FFT) y PSD o densidad espectral de potencia. 



![image](https://github.com/user-attachments/assets/12629597-a35b-487a-9910-8cbe188bb6f9)







*Normalizar las señales.*


Esta parte la realizamos para centrar en 0 o restar la media de cada señal, normalizar la varianza lo que es dividir entre la desviación estándar ya que eso mejorara la separación de señales con FastICA.




![image](https://github.com/user-attachments/assets/3cf85033-be6b-4a95-8d01-7f95acf4e166)







*Separacion de fuentes con FastICA.*


En esta parte se aplica Análisis de componentes independientes (FastICA) para lograr separar las fuentes de sonido, para asi obtener 3 señales separadas que son las voces individuales.




![image](https://github.com/user-attachments/assets/a24d9fb1-6d8d-4009-85c6-d9d586bcbb5a)



*Selección fuente con mayor energía.*


Calcula la energía de cada audio y selecciona la que tenga mayor energía.

![image](https://github.com/user-attachments/assets/cbffb089-d2ee-425c-9d2d-57d5eaf2ac08)






*Graficar la voz aislada y cálculo de potencias.*


Muestra y guarda la gráfica de la voz separada en el tiempo, así como también hace el cálculo de las potencias para así poder mostrar los valores en la consola y luego hacer el cálculo del nuevo SNR.




![image](https://github.com/user-attachments/assets/63923c4c-95c1-4f3f-ae13-ad73b818fe83)






*Guardar y reproducir la voz aislada.*



Guardar un archivo con la voz aislada y lo reproduce en el sistema operativo deseado. 




## Métodos de separación de fuentes
La separación de fuentes de audio es una técnica de procesamiento de señales que se usa para separar y aislar diferentes sonidos, como puede ser la voz. En otras palabras, es el proceso de extracción de señales de sonido individuales de una mezcla de varias señales en una grabación de audio.
Existen diferentes métodos de separación de fuentes, entre ellos:

### Análisis de Componentes Independientes (ICA)
Consiste en un método estadístico para separar una señal en varios subcomponentes, esto con el propósito de estimar componentes independientes. Es un modelo lineal que supone que las variables observadas son una mezcla lineal de variables desconocidas no gaussianas. 

Para realizar este análisis se representan las señales como una combinación lineal, se aplica un modelo matemático para encontrar una transformación para la independencia de las señales y por ultimo se obtiene una señal aislada similar a la original.
### Beamforming 
Es una técnica de formación de haces (forma espacial de filtrado y usada para distinguir una señal objetivo y el ruido de fondo) encargada de dirigir una señal inalámbrica a una dirección concreta, evitando que se disperse en varias direcciones. Este método mejora el SNR de la señal deseada y atenúa el ruido de otras direcciones. 

Para realizar este método, se utilizan varios micrófonos en una configuración especifica, se aplican pesos a las señales captadas para alinearla en la dirección deseada y por último, se suma la señal alineada para cancelar el ruido de otras direcciones.  
Existen otros métodos para aislamiento de señales de interés como:

*Filtrado Adaptativo: minimizar el error entre la señal deseada y la interferencia

*Transformada de Fourier de Corto tiempo: analiza y filtra señales en el dominio de la frecuencia y espacio

*Redes neuronales: aprender patrones de ruido y mejora la separación de voz
### Diferencias entre ICA y Beamforming
*ICA
Funciona como mezclas de señales de diferentes fuentes, separa señales superpuestas independientes y opera en el dominio estadístico y matemático

*Beamforming
Se enfoca en una dirección específica mediante manipulación de micrófonos, funciona con señales espaciales y opera en el dominio espacial.

## Transformada Rápida de Fourier (FFT)
Es un método distinto de medición de audio, en donde se descompone una señal en sus componentes espectrales individuales y este proporciona información sobre su composición, este método es utilizado para análisis de errores, control de calidad y manejo de las condiciones del audio.  Este algoritmo calcula la Transformada Discreta de Fourier (DFT) la cual es una herramienta fundamental en el procesamiento de señales para convertir una señal en el dominio del tiempo al dominio de la frecuencia. 
La transformada Discreta de Fourier analiza todas las frecuencias discretas y proporciona una representación espectral de la señal y está dada por la siguiente ecuación: 
![image](https://github.com/user-attachments/assets/412520c5-31f9-454a-8a43-2c10184719e2)

*Ecuación de Transformada Rápida de Fourier (FFT)*

La FFT es una algoritmo que reduce la complejidad computacional para que el calculo de la DFT sea aún más rápido. 
Para este laboratorio se tomaron las audio grabados y se hallo la Transformada Rapida de Fourier y se obtuvieron las siguientes graficas: 
![image](https://github.com/user-attachments/assets/87deff14-2305-4a53-b9b5-0373baac657e)




*FFT en las señales de audio obtenidas*

En esta grafica se evidencia el análisis en frecuencia mediante la FFT, la cual convierte la señal en el dominio del tiempo al dominio de la frecuencia, de igual manera permite identificar que frecuencias están presentes en la señal y con qué intensidad.

Analiza así la estructura espectral de la señal de audio, en el eje x representa las frecuencias en un rango de 0-8000 Hz (frecuencia de muestreo = 16KHz) y en el eje y se logra ver la intensidad, es decir la amplitud de cada componente de frecuencia, un valor más alto de frecuencia indica que la señal tiene mayor energía. En las tres graficas se observan picos en bajas frecuencias y la energía rápidamente disminuye en frecuencias más altas (sugiere que el ruido no es dominante en la región del espectro), esto indica que la mayor parte de la señal está en frecuencias bajas, esto corresponde a una característica de la voz humana. 

## Densidad Espectral de potencia
Es una medida de la distribución de potencia sobre el rango de la frecuencia, da a conocer la distribución de potencia de una señal especifica sobre las distintas frecuencias en donde se forma. Se logra establecer el rango de frecuencias donde se concentran las variaciones de potencia. 

Permite entender que frecuencias dominan en la señal y como se distribuye la energía en el espectro. Por medio de esta densidad en el caso de una señal de audio se pueden identificar las frecuencias dominantes de una señal.
En este laboratorio se obtuvo tres resultados de señales para cada persona y con cauda una se realizo la densidad espectral de potencia y se logro ver las siguientes graficas:

![image](https://github.com/user-attachments/assets/5a5879a6-172a-4454-847b-c6c200a48dfb)

*Graficas de la densidad espectral de potencia*

 
Se observan las tres señales donde se mide la distribución de potencia de la señal en el dominio de la frecuencia. En el eje x podemos observar las frecuencias de la señal y los componentes dominantes de 100 a 1000 Hz y se evidencia la voz. Por otra parte, en el eje y se observa la cantidad de energía presente para cada frecuencia y los valores más altos se identifican como que la señal tiene más potencia en estas frecuencias. 


Teniendo en cuenta los conceptos anterioreres se pueden ver los siguiente sresultados.
![image](https://github.com/user-attachments/assets/52f9e8d8-85dc-4ead-bdc8-5b6ac8881407)




*SNR de cada una de las fuentes.*



Se realizó el cálculo de SNR (Signal to Noise Ratio) de cada una de las señales de audio en las cuales se obtuvieron los siguientes datos:
SNR de audio-santi.wav: 16.55 dB
SNR de audio-melany.wav: 16.13 dB
SNR de audio-majo.wav: 18.70 dB
Normalmente cuando el SNR de una señal es mayor a 10 dB se entiende que la señal es aceptable y cuando están por encima de 20 dB es una señal con muy buena calidad
Por lo que podemos analizar de los resultados obtenidos que el audio de majo cuenta con SNR más alto, es decir, una mejor relación señal ruido con una mejor calidad de audio comparado a los otros dos audios y por otro lado los audios de Melany y Santi son bastante similares, pero con un valor menor a la anterior, lo cual indica que contiene un poco más de ruido. Gracias a lo anterior se puede deducir que los SNR depende de los micrófonos utilizados, el lugar de grabación y la alta presencia de ruido que había en el lugar.




![image](https://github.com/user-attachments/assets/110282b8-bcd5-4998-bd9a-9a05732188c6)






*SNR audio separado.*




Un valor de 56,56 dB indica que la voz es significativamente más fuerte que el ruido del lugar ya que si se observa de forma general un SNR mayor a 40 dB se considera como una muy buena señal, pero en este caso también podemos observar que el audio no es del todo de la mejor calidad, pero el valor de la potencia del ruido indica que el método utilizado para la separación de la voz fue bastante bueno puesto que es bastante baja. 




Se obtuvo la siguiente señal separada del audio de majo. 


![image](https://github.com/user-attachments/assets/404de6fe-a6a6-433f-a789-9afa11f18602)





*Voz separada.*



De acuerdo a esta grafica se puede deducir que entre 0 y 5 segundos la amplitud es baja puesto que en ese momento fue el tiempo de silencio para tomarlo como ruido, pero existían ruidos muy suaves del ambiente como la música que se encontraba en un lugar cerca, luego de los 5 segundos la amplitud aumenta lo que indica que es cuando se vuelve fuerte el habla, asi como la señal también muestra picos bastante elevados lo que significa que hubo sonidos más fuertes por momentos.
Por otro lado, se evidencia que la voz sufro distorsiones puesto que no se hizo un buen trabajo de almacenamiento de componentes espectrales que son fundamentales en el habla y es por esto que la voz suena como si hablara un robot. 




## Requisitos:
• Python 3.9


•	Librosa



• Numpy




• Matplotlib



• Soundfile

• Os

• Scipy.fftpack

• fft, fftfreq

• Sklearn.decomposition

• Scipy.signal 

## Contactanos:
•est.mariajose.perez@unimilitar.edu.co




•est.melany.gonzalez@unimilitar.edu.co





•est.david.smoreno@unimilitar.edu.co
## Bibliografia:
• Beamforming. (s/f). Lowi.es. Recuperado el 7 de marzo de 2025, de https://www.lowi.es/glosario/beamforming/

• FFT. (s/f). Nti-audio.com. Recuperado el 7 de marzo de 2025, de https://www.nti-audio.com/es/servicio/conocimientos/transformacion-rapida-de-fourier-fft

• Luengas C., L. A., & Toloza, D. C. (2020). Análisis frecuencial y de la densidad espectral de potencia de la estabilidad de sujetos amputados. TecnoLógicas, 23(48), 1–16. https://doi.org/10.22430/22565337.1453

• Separación de Fuenttes de audio. (s/f). Sciencedirect.com. Recuperado el 7 de marzo de 2025, de https://www.sciencedirect.com/topics/computer-science/audio-source-separation






