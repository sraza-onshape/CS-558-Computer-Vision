import argparse

from util import ops
from util.gaussian_derivative import GaussianDerivativeFilter

def main():
    """Main function of the script."""

    # input and output arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--operation",
        required=False,
        type=str,
        default='detect_edges',
        help="Which filtering function to use. Expected to be either 'smooth' (Gaussian filtering) or 'detect_edges' (computing magnitude of the image gradient)."
    )
    parser.add_argument(
        "--data",
        type=str,
        required=False,
        default="./original_images_cs558_bw1/plane.pgm",
        help="Path to input images."
    )
    parser.add_argument(
        "--image_name",
        type=str,
        required=False,
        default="Image",
        help="Caption of the image scene. Used in the plot of the output image"
    )
    parser.add_argument(
        "--sigma",
        required=False,
        default=1,
        type=int,
        help="Determines the extent of the smoothening by the Gaussian filter. Expects an int."
    )
    parser.add_argument(
        "--apply_non_max_suppression",
        required=False,
        type=bool,
        default=True,
        help="Whether or not to use non-max suppression. Ignored if --operation != 'detect_edges'."
    )
    parser.add_argument(
        "--threshold",
        required=False,
        type=bool,
        default=True,
        help="Threshold to use (for clipping the gradient magnitude). Ignored if --operation != 'detect_edges'."
    )
    parser.add_argument(
        "--padding_type",
        required=False,
        type=bool,
        default=True,
        help="Type of padding to use during the convolution(s). Expected to be one of 'zero' (zero-padding) or 'repeat' (replicates boundaries)."
    )
    args = parser.parse_args()

    # read the data
    image_obj = ops.load_pgm(args.data)
    
    # peform the appropiate function
    if args.operation == "smooth":
        ...
    else:  # args.operation == "detect_edges"
        GaussianDerivativeFilter.detect_edges_and_visualize(
            image=[image_obj],
            image_name=args.image_name,
            sigma=args.sigma,
            threshold=args.threshold,
            use_non_max_suppression=args.apply_non_max_suppression,
            padding_type=args.padding_type
        )


if __name__ == "__main__":
    main()