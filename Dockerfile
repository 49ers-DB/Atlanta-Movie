FROM continuumio/miniconda3
RUN conda create -f atlanta_movie_env.yml
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
