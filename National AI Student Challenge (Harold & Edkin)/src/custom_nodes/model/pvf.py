from typing import Any, Dict

import cv2
import numpy as np
import tensorflow as tf

from peekingduck.pipeline.nodes.node import AbstractNode

IMG_HEIGHT = 180
IMG_WIDTH = 180


class Node(AbstractNode):
   """Initializes and uses a CNN to predict if an image frame shows a normal
   or defective casting.   """

   def _init_(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
      super()._init(config, node_path=name_, **kwargs)
      self.model = tf.keras.models.load_model(self.weights_parent_dir)

   def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
      """Reads the image input and returns the predicted class label and
      confidence score.

      Args:
            inputs (dict): Dictionary with key "img".

      Returns:
            outputs (dict): Dictionary with keys "pred_label" and "pred_score".
      """
      img = cv2.cvtColor(inputs["img"], cv2.COLOR_BGR2RGB)
      img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
      img = np.expand_dims(img, axis=0)
      predictions = self.model.predict(img)
      score = tf.nn.softmax(predictions[0])

      return {
            "pred_label": self.class_label_map[np.argmax(score)],
            "pred_score": 100.0 * np.max(score),
      }
