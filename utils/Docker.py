import docker
import env

class Docker:
    def __init__(self) -> None:
        self.client = docker.from_env()
        self.registry = env.DOCKER_REGISTRY

    def remove_containers(self):
        try:
            containers = self.client.containers.list(all=True)  
            for container in containers:
                print(f"Removing container {container.id}")
                container.remove(force=True) 
            print("All Docker containers removed successfully")
        except docker.errors.APIError as e:
            print(f"API Error: {str(e)}")

    def remove_images(self):
        try:
            images = self.client.images.list()
            for image in images:
                print(f"Removing image {image.id}")
                self.client.images.remove(image.id, force=True) 
            print("All Docker images removed successfully")
        except docker.errors.APIError as e:
            print(f"API Error: {str(e)}")

    def logout(self):
        try:
            self.client.api.logout(self.registry) 
            print("Successfully logged out of Docker")
        except docker.errors.APIError as e:
            print(f"API Error: {str(e)}")