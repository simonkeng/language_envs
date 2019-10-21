FROM python

RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install click

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils
RUN apt-get update && \
    apt-get install -y vim && \
    apt-get install -y zsh && \ 
    apt-get install -y curl

RUN git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
RUN sh ~/.vim_runtime/install_awesome_vimrc.sh

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

COPY config/ /root/config/
RUN mv /root/config/.zshrc /root/.zshrc

RUN git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
RUN yes | ~/.fzf/install
CMD ["source", "~/.zshrc"]


