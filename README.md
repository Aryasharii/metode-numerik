# Tugas Besar Metode Numerik

Ini adalah repositori untuk proyek tugas besar mata kuliah Metode Numerik di UPer.

### Table of contents

- [Projek Tugas Besar Metode Numerik](#kelompok7-iot-project)
    - [Table of contents](#table-of-contents)
- [Main Project: Smart Incubator ](#main-project-smart-incubator-)
    - [Problem Statement ](#problem-statement-)
    - [Our Solution ](#our-solution-)
    - [Use case diagram ](#use-case-diagram-)
    - [Hardware ](#hardware-)
      - [Hardware Setup ](#hardware-setup-)
    - [Communication Protocol ](#communication-protocol-)
    - [Cloud Platform \& Web server ](#cloud-platform--web-server-)
    - [Dashboard Frontend ](#dashboard-frontend-)
- [Updates ](#updates-)
    - [Milestone 4: Send sensor data to database, Flask server reads data from database ](#milestone-4-send-sensor-data-to-database-flask-server-reads-data-from-database-)
- [Milestones Demo Videos Rewind ](#milestones-demo-videos-rewind-)

<br/>

# Main Project: Smart Incubator <a name="project"></a>

### Problem Statement <a name="prob"></a>

> **tldr**: _Inconvenient for dorm residents to physically check if shared washing machine is available to use._

```
Chicken eggs require precise temperature control for proper incubation and hatching.

Traditionally, egg incubators rely on manual adjustments or basic thermostat mechanism, which are susceptible to fluctuations and errors. This can lead to inconsistent hatching rates and the mortality of chicks.

The environment experiences temperature variations throughout the year, making it difficult to maintain a consistent temperature in the incubator.

Farmers don't have a lot of choice except,
- turn on the light manually, OR
- Set the time to turn on the light automaticly.

They have to go to the incubators & manually turn on the light or set time to turn on the light automaticly.

Manual adjustments
Traditional incubators require frequent manual adjustments to temperature settings, which can be time-consuming and prone to human error.

Limited monitoring
Current incubators often lack real-time temperature monitoring capabilities, making it difficult to identify and address temperature fluctuations promptly.

Imagine the farmers should get 100 eggs, but because of the temperature the farmers only get 90% of it.

With this IoT, the farmer will get notification of the temperature of incubators and the light will do their job to adjust the temperature for your eggs.
```

<br/>

### Our Solution <a name="sol"></a>

A full stack IOT application to automate the checking if the temperature in incubator is stable nor in range, and will automaticly adjust the light (turn on/off).

<br/>

### Use case diagram <a name="uc"></a>

![Use case diagram](https://github.com/Aryasharii/Kelompok7-IoT-Project/blob/master/UML%20Diagram/Use%20Case%20Diagram_IoTProject.png)

**Tentative features**

- none
<br/>

<!-- ### System Architecture <a name="sysarc"></a>
![Overview of the tech stack](https://github.com/Rekanice/swe-G2-iot-project/blob/e0d91b83c3a7868e55449eced2450638003cc4a4/images/system_arch_pic.png) -->

<br/>

### Hardware <a name="hw"></a>

<!-- ```
- Sensor : RGB light sensor module
- MCU    : NodeMCUv1 ESP8266
``` -->
<!-- ![Light Module sensor from Cytron](https://github.com/Rekanice/swe-G2-iot-project/blob/f124691cfb8c146144e130dbb8553d363e562a06/images/light_sensor_module.jpg)
![NodeMCU ESP8266](https://github.com/Rekanice/swe-G2-iot-project/blob/e8a1b532913f9c267a11f2c236fd56e05f51c070/images/nodemcu_ESP8266.jpg) -->
- Sensor    : DHT11
- MCU       : ESP32
- Indicator : LED, Telegram Bot Notification
<br/>

#### Hardware Setup <a name="hwsetup"></a>

<!-- ![Device setup](https://github.com/Rekanice/swe-G2-iot-project/blob/d76a08e94ea6444962755b7ac9bf270c3a8d7b9a/images/device_setup.jpg) -->

<br/>

### Communication Protocol <a name="comm"></a>

The communication protocol used in this project is API based. Data from DHT11 will sent every 1 minutes or when users do commands, to Telegram bot then Temperature and Humidity will show as notification or chat from Telegram bot. 

<br/>

### Cloud Platform & Web server <a name="cloud"></a>

<!-- ```
Backend framework      : Flask
Cloud hosting platform : Heroku
```
Check out our Flask toy app [here](https://tell-me-something-flask-app.herokuapp.com/)

Check out our Django toy app [here](https://this-is-django-1.herokuapp.com/)

Here is a [video](https://youtu.be/oEzaFD8RCEE) of deploying the Flask/Deploy app in Heroku.

This is the accompanying article on [Deploying the Flask / Django app in Heroku](https://github.com/Rekanice/swe-G2-iot-project/blob/f4e41c6ab807bea9e7c15f0c16e89c8eff10dd4d/Deploying-on-Heroku.md). -->

<br/>

### Dashboard Frontend <a name="ui"></a>

<!-- ```
Web    : Basic HTML-CSS-JS
Mobile : MIT Inventor
```

Here is a [demo video](https://www.youtube.com/watch?v=bYe--Yvlxbc) of the mobile app prototype made in MIT App Inventor. -->

<br/>

**UI Wireframe - Version 1**

<!-- [Figma Design of the UI](https://www.figma.com/file/upOI1YDz3MclTJADYTzi7z/Figma-UI?node-id=0%3A1)


![page1](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page1.png)
![page2](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page2.png)
![page3](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page3.png)
![page4](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page4.png)
![page5](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page5.png) -->

<br/>

# Updates <a name="updates"></a>

<!-- ### Milestone 3: Send sensor data directly to Flask server <a name="mi3"></a>

The ESP8266 sends the light sensor data to the Flask web server hosted on Heroku via HTTP POST requests. The Flask web app dynamically updates the status of the washing machine display box, with a ~5s delay (this is negligible in real use case) without the user needing to refresh the page.

[Heroku web app](https://idle-washer.herokuapp.com/)

[Demo video for milestone 3](https://youtu.be/WuiT0wlSRcE)

![Sensor setup](https://github.com/Rekanice/swe-G2-iot-project/blob/bbef47352ffa9df50c8eafda36a5559154607df4/images/ldr.jpg)

![Flask web server UI](https://github.com/Rekanice/swe-G2-iot-project/blob/bbef47352ffa9df50c8eafda36a5559154607df4/images/flaskwebhtml.png) -->

<br/>

### Milestone 4: Send sensor data to database, Flask server reads data from database <a name="mi4"></a>

<!-- The ESP8266 sends the light sensor data to the Flask web server hosted on Heroku via HTTP POST requests. The Flask server has a dedicated url to accept & parse the POST request & store the data into the connected PostgreSQL database. The Flask web app dynamically updates the UI by querying necessary data from the database, and processing them in the application to be delivered in the UI templates.

[Demo video for Milestone 4](https://youtu.be/-4hxKUfy3Ok)

Database tables design:
1. Washing_Machine : contains all the attributes about the washing machines.
![Washing Machine table](https://github.com/Rekanice/swe-G2-iot-project/blob/b5c75e600e6379d77504918cd4bc5cbfa9e4ab16/images/db_table_washing_machines.jpg)

2. Sensor_Log: records the detected light data from a given washing machine (identified by its wm_id), every 5 minutes. The two tables are linked by the wm_id column.


![Sensor log table](https://github.com/Rekanice/swe-G2-iot-project/blob/b5c75e600e6379d77504918cd4bc5cbfa9e4ab16/images/db_table_sensor_log.jpg)

![Flask web server UI](https://github.com/Rekanice/swe-G2-iot-project/blob/b5c75e600e6379d77504918cd4bc5cbfa9e4ab16/images/flask_webpage_with_static_heatmap.jpg) -->

<br/>

<!-- ### Milestone 5: Dashboard UI improvements <a name="mi5"></a>

From the feedback on the dashboard in milestone 4, these changes were made:
- more washing machine indicators
- a more recent timeline plot (hence, we went with the last hour readings in 5 minute intervals)
- a more dashboard box-style layout

All the data required by the dashboard to display are served via APIs in the Flask app.py. The necessary data are queried from the PostgreSQL database and processed before passing to the frontend.


The repository for cloning and reproducing our milestone 5 Flask app is transferred to a new repository ([link here](https://github.com/Rekanice/Check-WM-Dashboard)).


[Youtube Demo for Milestone 5](https://youtu.be/qwATc6cMqR8)

![How the new dashboard looks like](https://github.com/Rekanice/swe-G2-iot-project/blob/fe0e162c5e2c1b701822b52d4fc0dace6c6adb8d/new_dashboard.png) -->

<br/>

# Milestones Demo Videos Rewind <a name="rewind"></a>

<!-- 1. Milestone 1 [Part 1](https://youtu.be/BIsVwdGV0DI) [Part 2](https://youtu.be/cB8r0cHiGOs) [Part 3](https://youtu.be/qsbzFyFUOwY)
2. Milestone 2 [Heroku Deployment](https://youtu.be/oEzaFD8RCEE) [UI Prototype](https://www.youtube.com/watch?v=bYe--Yvlxbc)
3. [Milestone 3 video](https://youtu.be/WuiT0wlSRcE)
4. [Milestone 4 video](https://youtu.be/-4hxKUfy3Ok)
5. [Milestone 5 video](https://youtu.be/qwATc6cMqR8) -->
