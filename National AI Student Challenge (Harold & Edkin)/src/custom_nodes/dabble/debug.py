"""
Node template for creating custom nodes.
"""

from typing import Any, Dict
import numpy as np
from peekingduck.pipeline.nodes.abstract_node import AbstractNode


class Node(AbstractNode):
    """This is a template class of how to write a node for PeekingDuck.

    Args:
        config (:obj:`Dict[str, Any]` | :obj:`None`): Node configuration.
    """

    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)
        self.frame=0

        # initialize/load any configs and models here
        # configs can be called by self.<config_name> e.g. self.filepath
        # self.logger.info(f"model loaded with configs: config")

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:  # type: ignore
        if "person" in inputs["bbox_labels"]:
            print(
                #f"{self.frame} {inputs['keypoints'][np.where(inputs['bbox_labels'] == 'person'),0,0]}"
                f"{self.frame}{inputs['keypoints'][0,10]}"
            )
        self.frame += 1
        return {}
        # result = do_something(inputs["in1"], inputs["in2"])
        # outputs = {"out1": result}
        # return outputs
