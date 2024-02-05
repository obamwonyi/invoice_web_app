    # The first instruction is what image we want to base our container on
    FROM python:3.8

    # The environment variable ensures that the python output is set straight
    # to the terminal without buffering it first
    ENV PYTHONUNBUFFERED 1

    # Set the working directory to your working directory
    WORKDIR /DRF

    # Copy the requirements file to the container
    COPY requirements.txt requirements.txt

    # Install any needed packages specified in requirements.txt (this would be 
    # created)
    RUN pip install -r requirements.txt
