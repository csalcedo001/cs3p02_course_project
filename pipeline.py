import kfp
from kfp import dsl
import kfp.components as comp

@dsl.pipeline(name='xor-training')
def simple_pipeline(
        train_size:int=100,
        test_size:int=10,
        dims:int=2,
        size_hidden:int=16,
        num_hidden:int=1,
        epochs:int=5,
    ):

    # Load components
    xor_sampler_comp = comp.load_component_from_file('components/xor_sampler.yaml')
    sample_scatter_comp = comp.load_component_from_file('components/sample_scatter.yaml')
    train_comp = comp.load_component_from_file('components/train.yaml')
    training_plots_comp = comp.load_component_from_file('components/training_plots.yaml')

    # Define pipeline
    op_xor_sampler = xor_sampler_comp(dims=dims, train_size=train_size, test_size=test_size)

    with dsl.Condition(dims == 2):
        op_sample_scatter = sample_scatter_comp(input_dir=op_xor_sampler.output)

    op_train = train_comp(
        input_dir=op_xor_sampler.output,
        model='simplenet',
        dims=dims,
        size_hidden=size_hidden,
        num_hidden=num_hidden,
        epochs=epochs)
    
    training_plots_comp(model_dir=op_train.output, model_name='simplenet')


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(simple_pipeline, __file__ + '.yaml')
