# test_queue.py
from clearml import Task

task = Task.init("Dale's Playground", 'Some Task')

task.set_script(
    repository='https://github.com/dalegeorg-clearml',
    branch='master',
    working_dir='testing',
    entry_point='test.py')

task.execute_remotely("dale")
