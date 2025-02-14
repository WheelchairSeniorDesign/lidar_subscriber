from setuptools import find_packages, setup

package_name = 'livox_data_logger'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),  # find_packages() finds the subfolder
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bad',
    maintainer_email='bad@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # adding the results to log:
            'livox_data_saver = livox_data_logger.livox_data_saver:main',
        ],
    },
)
