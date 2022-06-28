import kfp
from kfp import dsl
import kfp.components as comp

@dsl.pipeline(name='ejemplo-simple')
def simple_pipeline():
    generate_data = comp.load_component_from_file('component.yaml')
    op_gen = generate_data()

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
