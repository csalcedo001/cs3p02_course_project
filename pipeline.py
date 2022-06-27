import kfp
from kfp import dsl

@dsl.pipeline(name='ejemplo-simple')
def simple_pipeline():
    op_gen = dsl.ContainerOp(
        name='generador',
        image='python:alpine3.7',
        command=[
            'python',
            '-c'
        ],
        arguments=[
            "import random; import json; json.dump([random.randint(0, 100) for _ in range(5)], open('/tmp/out.json', 'w'))"
        ],
        file_outputs={'out': '/tmp/out.json'},
    )

    with dsl.ParallelFor(op_gen.output) as e:
        dsl.ContainerOp(
            name='prob-de-elemento',
            image='library/bash:4.4.23',
            command=['sh', '-c'],
            arguments=['echo Probabilidad de obtener {} de la distribucion: 0.01'.format(e)],
        )

    dsl.ContainerOp(
        name='promedio',
        image='python:alpine3.7',
        command=['sh', '-c'],
        arguments=['echo Promedio de los numeros: && python -c "print(sum({0})/len({0}))"'.format(op_gen.output)],
    )

    dsl.ContainerOp(
        name='suma',
        image='python:alpine3.7',
        command=['sh', '-c'],
        arguments=['echo Suma de los numeros: && python -c "print(sum({}))"'.format(op_gen.output)],
    )


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(simple_pipeline, __file__ + '.yaml')
