import docker
import containers, image
import datetime

client = docker.from_env()

def main():
    if not containers.running_properties():
        print('[INFO] {0:%Y-%m-%d %H:%M:%S} No containers are running'.format(datetime.datetime.now()))
    else:
        for running_container in containers.running_properties():
            current_image = client.images.get(running_container["ImageID"])
            latest_image = image.pull_latest(current_image)
            # if current running container is running latest image
            print(image.is_up_to_date(current_image.id, latest_image.id))
            # new container object to create new container from
            print(containers.NewContainerProperties(running_container, latest_image.tags[0]).__dict__)
if __name__ == "__main__":
    main()