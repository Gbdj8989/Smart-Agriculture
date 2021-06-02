# Smart-Agriculture
**Abstract** - Smart farminis an emerging concept, as IoT sensors can provide information on agricultural fields and operate according to user input. It is proposed to establish a Smart Agriculture System that utilizes the benefits of cutting-edge technologies such as Arduino, IoT and g Wireless Sensor Network. Environmental monitoring is a major factor in improving crop yields. Includes the development of a system that can monitor temperature, humidity.

### <div align="center">I.  INTRODUCTION</div>
Agriculture contributes about 17% of India's GDP where the 70% rural population depends on it. With old farming practices, the natural resources like water upon which agriculture depends are used injudiciously. More and more use of fertilizers and pesticides has caused a decrease in the quality of food. Irregular rainfall and wind pattern and sudden change in climatic conditions affects the crop in a negative way. So, this project aims at creating a decision system along with an early warning system to support agriculture in a more precision fashion.
### <div align="center">II.  STUDY OF SIMILAR PROJECTS OR TECHNOLOGY</div>
1.  Data visualization with Chat.js
2. Crop Water Requirement and Irrigation scheduling of Soybean and Tomato crop using CROPWAT 8.0 
### <div align="center">III.  CONCEPTS USED</div>
#### 1.	Smart Irrigation System 
The loss of water in crops is mainly caused by evaporation from soil surface and transpiration loss from the leaf surface. These two losses together are called evapotranspiration loss. This loss of water can be met up by natural watering (rainfall) or by irrigation. Irrigation is providing water to crops artificially from sources like rivers, lakes, canals, and underground water. Irrigation depends upon various factors like present weather conditions with temperature, rainfall, humidity, the amount of sunlight falling on the soil and crop canopy cover. With existing framing practices, all the factors were impossible to be implemented due to lack of knowledge to the farmers. This project aims at creating a decision system incorporating the factors through various sensors.
#### 2.	Crop Health Detection 
The crop health is an essential parameter to know what stages of growth the crop is and how is the health of the crop at that stage. Crop health is assessed with the use of hyperspectral imaging by several vegetation indices like NDVI and EVI. The images are processed into a number and that number states the crop health in accordance with the index. This project uses NDVI. It is a simple graphical tool that uses the Near Infrared and Red spectrum. The index is provided below. 
 |NDVI|Crop Health Status|
|----|------------------|
|From -1 to 0|Dead plants or inanimate objects| 
|From 0 to 0.33|Unhealthy|
|From 0.33 to 0.66|Moderately healthy|
|From 0.66 to 1|Healthy|
#### 3.	Pest infestation warning and alert
It may happen that the crops may be infested by pest. It can happen due to many causes like seasonal changes, weather changes or food/water shortage. Pest can be detected by uploading image(s) on the portal of different parts of the plant. The backend AI assess the health of the crops and notify if it is healthy or has some disease. In the project there can be 4 types of result which includes healthy, scab, rust, and other multiple diseases. It uses prebuilt classifier. 
### <div align="center">IV.  MODEL TOOL</div>
#### Smart Irrigation System
Sensors Used:
a.	Capacitive soil moisture sensor: It is an analog sensor that uses capacitors to store charges when in contact with moist substance. The amount of charging is proportional to the amount of water present in the soil.

b.	Photoresistors: Commonly called Light Dependent Resistors (LDR) is an analog sensor. The analog value is proportional to the amount of light (luminance)

c.	DHT sensor: A humidity and 	temperature sensor (DHT-11/22) is a digital sensor that provides information about the humidity and temperature of a surroundings.

Integration: All the sensors are connected to a ESP8266 development board called NodeMCU through wiring.

Architecture Used: The data sensed by the sensors are transmitted to a Raspberry Pi (a local server and itself a development board) by a Wireless Network (Wi-Fi) using Message Queueing Telemetry Transport (MQTT) from the NodeMCU. The MQTT broker used is a local broker called Mosquitto. The topics were created in the nomenclature of “_gridNumber_/_sensorName_”. 

For future study of the data and reference, the data collected in real time by the sensors are stored in a local NoSQL database using MongoDB. A python script is daemon into the raspberry pi for the purpose.

#### Crop Health Detection
Normalized Difference Vegetative Index (NDVI) was obtained from the satellite data provided by  Agro API. The data provided by the API is historical thus providing a better understanding of the curve giving the farmers to analyze their crop.
#### Pesticide Infestation Warning and Alert
We build a machine learning algorithm to correctly classify if a plant is healthy, has a stem rust or has leaf rust or multiple diseases. A Hierarchical Data Format version 5 (hdf5) life is produced by using 10000s of different types of infested plants. Of the various steps in the pipeline. Data Augmentation particularly played a significant role in increasing the model performance. The overall modelling process required several steps for effectively preparing the data for the CNN model to yield a good result.
#### Portal
Portal was developed with the technology stack

1.	Django – Backend 

2.	HTML, CSS, JS – Frontend 

3.	Chart JS – for data visualization

4.	OpenWeatherMap API – weather

5.	AgroApi – Satellite NDVI 

The portal acts as user interface for the users for seamless performance and providing apt notification like the weather for a given day and forecast for 8 days which gives the users a way to control how much water to provide the users. The portal also allows to upload the pictures of the plant leaf for Pest Infestation Warning and classifying which type of pest has attacked so that the spread of the pest could be kept minimal. It also enables the user to check their farmland’s Normalized Difference Vegetative Index through which the user/farmer has a knowledge about the crop health whole wide across the field.

###  <div align="center">V.  IMPLEMENTATIONS AND RESULT
#### Smart Irrigation System
The testing of this module was performed in a small pot where a capacitive moisture sensor was used. The experiment was performed on a sunny day. The field was divided into grids and sensors were placed. When the soil moisture level dipped below 30%, the irrigation pump ran by relay was switched on. When the moisture level went up to 90%, the pump stopped. 
#### Crop Health Detection
A field was chosen in random with the GPS coordinates, the polygon/ field borders were done through GeoJSON into the AgroAPI. The date was sent to the portal were by it is clear the trends of the crop health.
#### Pesticide Infestation Warning and Alert
Photos of some leaves were clicked and uploaded into the portal.
The dataset formed had a quite good accuracy of 92%.
#### Portal
![alt text](https://github.com/subhidh/Smart-Agriculture/blob/main/portal%20screenshot/Picture2.jpg)
![alt text](https://github.com/subhidh/Smart-Agriculture/blob/main/portal%20screenshot/Picture1.jpg)
![alt text](https://github.com/subhidh/Smart-Agriculture/blob/main/portal%20screenshot/Picture3.jpg)
![alt text](https://github.com/subhidh/Smart-Agriculture/blob/main/portal%20screenshot/Picture4.jpg)
### <div align="center">VI.  CONCLUSION
For future scope, there are wide aspects that needs to be covered like creating an automated scientific crop specific irrigation system, creating a reliable and efficient Wireless Sensor Network
### <div align="center">VII.  REFERENCES
1.  G. Sushanth and S. Sujatha, "IOT Based Smart Agriculture System," 2018 International Conference on Wireless Communications, Signal Processing and Networking (WiSPNET), 2018, pp. 1-4, doi: 10.1109/WiSPNET.2018.8538702.

2. Rehman, Aqeel-ur & Shaikh, Zubair. (2009). Smart Agriculture. 10.2174/978160805077210901010120.

3. S. R. Prathibha, A. Hongal and M. P. Jyothi, "IOT Based Monitoring System in Smart Agriculture," 2017 International Conference on Recent Advances in Electronics and Communication Technology (ICRAECT), 2017, pp. 81-84, doi: 10.1109/ICRAECT.2017.52.
