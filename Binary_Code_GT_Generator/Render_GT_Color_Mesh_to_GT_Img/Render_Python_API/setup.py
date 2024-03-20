from distutils.core import setup, Extension

module = Extension('Render',
                    include_dirs = ['$HOME/miniforge3/envs/BinaryCodeGen/include','..','$HOME/miniforge3/envs/BinaryCodeGen/lib/python3.11/site-packages/numpy/core/include',
                    '$HOME/code/project-jl2-camozzi/zebra_pose/ZebraPose/Binary_Code_GT_Generator/Render_GT_Color_Mesh_to_GT_Img/render_related_source/glad/include/'],
                    libraries = ['opencv_core', 'opengl_render'],
                    library_dirs = ['$HOME/miniforge3/envs/BinaryCodeGen/lib', '$HOME/code/project-jl2-camozzi/zebra_pose/ZebraPose/Binary_Code_GT_Generator/Render_GT_Color_Mesh_to_GT_Img/build'],
                    sources = ['RenderModule.cpp'],
                    extra_compile_args=['-std=c++14'])

setup (name = 'Render_directory',
       version = '1.0',
       ext_modules = [module])

