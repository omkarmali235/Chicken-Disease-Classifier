import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time

from cnnClassifier.entity.config_entity import PrepareCallbacksConfig

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config


    
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        print("tensorboard_callback")
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
        print("tensorboard_callback :")
        print(tensorboard_callback)
        return tensorboard_callback
    

    @property
    def _create_ckpt_callbacks(self):
        model_checkpt = tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
        print("model_checkpt :")
        print(model_checkpt)
        return model_checkpt


    def get_tb_ckpt_callbacks(self):
        return [object(self._create_tb_callbacks()),
            object(self._create_ckpt_callbacks())
        ]
