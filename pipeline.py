import kfp
from kfp import dsl
import kfp.components as comp

@dsl.pipeline(name='xor-')
def simple_pipeline(
        train_size:int=100,
        test_size:int=10,
        dims:int=2
    ):

    xor_sampler = comp.load_component_from_file('components/xor_sampler.yaml')
    op_xor_sampler = xor_sampler(dims=dims, train_size=train_size, test_size=test_size)

    with dsl.Condition(dims == 2):
        sample_scatter = comp.load_component_from_file('components/sample_scatter.yaml')
        op_sample_scatter = sample_scatter(input_dir=op_xor_sampler.output)


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(simple_pipeline, __file__ + '.yaml')
