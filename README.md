# Random Football Generator

## Objective
The main objective of this project was to create an application that would generate random objects upon a set of predefined rules. The main architecture required me to create four different services, which would interact and work togeather.

Service 1, will render a Jinja2 temmplates and will communicate with the other three services (either through a get or a post request). 

Service 2/3, will both generate random objects (and return these objects to service 1) - get request.

Service 4, will generate an object using a set of predefined rules (i.e. is determined by the values generated in service three and four) and thus a post request.

This architecture can be seen in the image below:


## Overview
The project that I chose to create was a random football generator - whereby the end user can click on a button and will either score or miss. This outcome will be mainly dependent on the outcomes from service 2 & 3, such that the user only scores if the football team and stadium generated from these service 2 & 3 match (this is determined by service 4). 
To start this project, I first designed the infastructure that I will be running to make this project a success and gave me an idea, on how each service would interact with each other. 

However due to the time restraint I was unable to add in user login functionality - whereby an individual user is able to login and track the amount of goals he/she has scored. Furthermore, to make the application more rewarding to the end user - I could have implemented a prize system (and thus could possibly mean an additional service being created, that could possibly interact with service 4 directly and generate random prizes)

## Risk Assessment
Once the overall design was created for the application, it was extremely important for me to attach some of the risk attached to building and running the application and each service. This is extremly important in order to mitigate and reduce risk involved with producing and running an application.

The inital assessment can be seen below (the measures that have been implemented within the development of the application can be seen in green):

## Architecture
The technology used to create these services, are as follow:
- Trello
- VM: GCP Compute Engine
- Python
- Flask 
- Pytest
- Git
- Jenkins
- Ansible
- Docker (Docker Swarm and Docker Compose)
- Nginx (Reverse Proxy and Load Balancer)

To track the project I used Trello, and used a Kanban Board setup (which enforces the use of agile methodology). The project was broken down to different task and each tasks was assigned story points, taking into account MoSCoW prioritisation (i.e. the most important task are done first, and thus are assigned the highest story point). At first all task were kept within the product backlog and each task within the product backlog was in the order, dependent on the story points assigned earlier. Then task would be moved into the sprint backlog (which either could be many task or one, depending on the user story point) and then on to review (where it would need to pass an intial test done by me on the application). 

From the images below you can see my Trello Kanban Board:



The version control system used on this project was Git and was held in a repository on Github. The development of the application and each service was done on multiple branches, which thus gave me an isolated enviroment to work on the project (without disturbing the main code base). 

The services were futher isolated by there own python3 environment and a GCP compute engine. The main bulk of the services were built in flask, which is a micro web framework within python. 

The main focus of the project was to create a CI/CD pipeline, which would automate the building of the application (i.e. each service). Therefore improving software delivery to the end user (whilst not disrupting the end user experience).
To achieve the CI/CD pipeline, many VMs were used on GCP to create this one seamless enviroment from production to deployment. The main tool which created this pipeline was Jenkins (which was ran on its own VM). The Jenkin VM was set to test the application before containerisation and thus when these test were ran and were successful, it would deploy the application using docker swarm.
However, for us to containerise and deploy our application we have to configure our other VMs. Therefore we used a tool known as Ansible, which acted as our configuration management. For this project it was to setup on our manager node, worker node and the load balancer. It was focused around updating update our VMs (mentioned above), install any packages/softwares (i.e. docker), setup docker swarm (between worker and manager node) and nginx load balancer.    
In order to activate this automation, any push event within the develop branch - would activate the automated CI/CD pipeline (done through the user of a webhook).

Overall the architecture can be seen below:



## Testing
The testing phase of the application was built into the CI pipeline, whereby the test were mainly focused around if each service was producing the right outcome (i.e. the random generated objects). Any push event on the develop branch on github would activate a Jenkins build and thus consequently a test was done on the new build - if the test fails, the existing build of the application would remain (and thus the affects of an app not working would not be passed to the end user). From below, we can see the outcome of our test.

### Service 1

### Service 2

### Service 3

### Service 4


## Application
When the application is opened up we are greeted with a quick message, which tells the end user the purpose of the application and what to do. To run the application we click on the button 'spin' - this would send a get request to service 2 & 3 and that outcome is then sent to service 4, using a post request, this should return if the user scored or not.

Once the button was clicked, a new page is displayed - which would indicate if the user has scored or missed.

## Future
In the future for the application - I would love to implement a score system, which is able to take in a user login and would track the amount of goals scored and missed by the end user. This would make it more rewarding to the end user, further to this, the implementation of a reward system would be extremely critical in making the application more useful to the end user and give it a better purpose.

In a more technological update, I would like use ansible to also configure our Jenkins VM - as currently the installation of a Jenkins VM is done manually (and the setup of connecting to our manager, worker, and nginx vm's). Therefore if the application was scaled up to a much larger scale or the Jenkins VM goes down (is in our risk assessment) - it would be detrimental to our CI pipeline and is a very tedious and difficult process to setup another Jenkins VM (and thus automating this would be helpful, in making a cleaner CI pipeline).  
