Three steps to setup to deploy docker:

1. In a command line interface, navigate to the project root folder.

2. Build as a Docker image using docker build -t IMAGE_NAME . Don’t forget that trailing period behind IMAGE_NAME.


3. RUN nvidia-docker run -d -p $port_out:5000 -v /path/to/params:/root/params IMAGE_NAME python /root/app.py -p /root/params/PARAMS_FILE_NAME
   to make a container.
   
   For example:
   nvidia-docker run -d -p 80:5000 -v /home/wanqi/p:/root/params napp python /root/app.py -p /root/params/xception_params.pkl

For testing:
There is a user whose token is 'AAA'.