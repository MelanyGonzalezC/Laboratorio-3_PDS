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











