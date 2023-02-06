from pathlib import Path

from peekingduck.pipeline.nodes.dabble import fps
from peekingduck.pipeline.nodes.draw import bbox, legend
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo, posenet
from peekingduck.pipeline.nodes.output import media_writer, screen
from peekingduck.runner import Runner
from src.custom_nodes.dabble import debug

def main():
    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")
    
    visual_node = visual.Node(source=0)
    posenet_node = posenet.Node()
    yolo_node = yolo.Node(detect=["person"])
    bbox_node = bbox.Node(show_labels=True)

    fps_node = fps.Node()
    legend_node = legend.Node(show=["fps"])
    screen_node = screen.Node()

    media_writer_node = media_writer.Node(output_dir=str(Path.cwd() / "results"))

    runner = Runner(
        nodes=[
            visual_node,
            posenet_node,
            yolo_node,
            debug_node,
            bbox_node,
            fps_node,
            legend_node,
            screen_node,
            media_writer_node,
        ]
    )
    runner.run()


if __name__ == "__main__":
    main()