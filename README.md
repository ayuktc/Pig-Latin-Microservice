# Pig-Latin Translator Microservice

## Overview
In this project, I was able to develop a simple microservice that allows users to translate any english word, phrase, comment, or sentence into pig latin. I was able to accomplish this using Python, Flask, and Docker. In order to use the translator follow the instructions below. Avehay unfay! (Have Fun!)

## Install and Run
To get the translator up and running is quite simple. Once you have cloned the repository, using terminal go ahead and change directories into the project. 
For instance on Mac, if the project was on my desktop and I was in the root directory, I would `cd Desktop/translatorMicroservice`.

Now, that you are in the project directory you will just have to run two simple docker commands in order to launch the translator locally.

The first command is to build the image from a Dockerfile. The Dockerfile is already provided for you and to build the image run `docker build -t piglatin_translator .` . 

You can verify that the Docker image has been created by running `docker images`, which will return a list of the images.  Once, our image has been successfully created, we can use docker run to launch our translator. 

After running `docker run -it --name python-container -p 8080:8080 piglatin_translator`, open a browser and access http://127.0.0.1:8080. This will lead you directly to the Pig Latin Translator's web page.

You will initially be directed to a home page, upon clicking on `Let's Get Started!` you will be able to enter anything that you want translated to pig latin!

## Client Scripts

To run the client script just run `./pglatin.sh -w <word>`. 

`Example: ./pglatin.sh -w hello`

# Looking Ahead

Currently, the Pig Latin API returns an html response. However, one imporvement I would love to make is for the API to return a JSON response instead. 
