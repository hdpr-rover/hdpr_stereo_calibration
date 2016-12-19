# -*- coding: utf-8 -*-
# rot_ros2rock.py

"""Script to transform from rotation matrix to Euler angles

This script is used to transform the ROS stereo camera calibration values to
values compatible with ROCK. Specifically ROCK requires the extrinsic rotation
values in Euler angles, but ROS outputs a rotation matrix.

To use this script copy the R matrix values here and run the script.
"""

__author__ = "Karl Kangur"
__copyright__ = "Automation and Robotics Laboratories, ESTEC, ESA"
__email__ = "karl.kangur@esa.int"

from transformations import euler_from_matrix

# Example rotation matrices from previous calibrations
R_PanCam = [
    [0.9999836069278953, -0.00023240842049579273, -0.005721176609985654],
    [0.00024969509117660275, 0.9999954056106259, 0.0030209948694463113],
    [0.005720448220026696, -0.003022373895774856, 0.9999790706450792]]

R_BB2_ExoTeR = [
    [0.9999660994769407, 0.0005699291869359836, 0.008214321493291354],
    [-0.0005449675322442045, 0.9999952285201806, -0.0030407149258747483],
    [-0.008216015291007525, 0.003036135305535032, 0.9999616387517796]]

R_BB2_HDPR = [
    [0.9999870390662159, 0.003319240401543643, -0.0038606142955546962],
    [-0.0033187175431029043, 0.9999944829835148, 0.00014183230261522977],
    [0.0038610637719910705, -0.00012901817594629462, 0.9999925377425868]]

R_BB3 = [
    [0.9999876162340475, 0.0029113372885849562, -0.004036272257844812],
    [-0.0029047354547933014, 0.9999944355793884, 0.0016405249763808876],
    [0.004041025919864856, -0.0016287803573709855, 0.9999905085469873]]

# Print out the Euler angles
print euler_from_matrix(R_BB3, 'sxyz')
