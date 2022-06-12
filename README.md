# CS3P01 - Cloud Computing: Proyecto Final del Curso

El proyecto consiste en un servicio que permita

- Enviar y almacenar modelos de redes neuronales en la nube.
- Llamar a los modelos de forma remota para observar un resultado.
- Correr los modelos directamente en la nube.
- Descargar modelos de la nube.

Se planea usar los contenedores de [KubeFlow en Docker Hub](https://hub.docker.com/u/kubeflow) como base. En detalle:

1. Los contenedores con redes entrenadas seran deployados a un servidor.
2. El usuario podra realizar un request al servidor en el que pase el input para la red neuronal.
3. El servicio sera distribuido entre los contenedores que manejen el modelo para que procesen el input del usuario.
4. El output del modelo sera devuelto al usuario.

El servicio de KubeFlow ya esta activo en un servidor remoto de Amazon Web Services (AWS): https://2dfc-3-17-73-149.ngrok.io/#/pipelines.
