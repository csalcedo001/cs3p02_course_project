import kfp
from kfp import dsl
import kfp.components as comp

@dsl.pipeline(name='xor-training')
def simple_pipeline(
        train_size:int=10000,
        test_size:int=1000,
        dims:int=2,
        size_hidden:int=16,
        # num_hidden:int=1,
        epochs:int=1000,
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

    op_train_0 = train_comp(
        input_dir=op_xor_sampler.output,
        model='simplenet',
        dims=dims,
        size_hidden=size_hidden,
        num_hidden=0,
        epochs=epochs)

    op_train_1 = train_comp(
        input_dir=op_xor_sampler.output,
        model='simplenet',
        dims=dims,
        size_hidden=size_hidden,
        num_hidden=1,
        epochs=epochs)
    
    training_plots_comp(
        model_dir_0=op_train_0.output,
        model_name_0='0 hidden layers',
        model_dir_1=op_train_1.output,
        model_name_1='1 hidden layers',
    )


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(simple_pipeline, __file__ + '.yaml')
