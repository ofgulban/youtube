"""Upsample images."""

import os
import nibabel as nb
import numpy as np
from scipy.ndimage import zoom

# =============================================================================
INPUTS = [
     "/Users/faruk/data/video-siham/video/03_baby_MNI_templates/00_nihpd_obj2_asym_nifti/nihpd_asym_00-02_t1w.nii",
    ]

OUTDIR = "/Users/faruk/data/video-siham/video/03_baby_MNI_templates/01_upsample"

INTERPOLATION = 3  # 0 for nearest neighbor, 1 for linear, 3 for cubic

# =============================================================================
# Output directory
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
print("  Output directory: {}".format(OUTDIR))

# =============================================================================
print("\n  Upsampling 2X...")

for i in INPUTS:
    print(f"\n    Loading data: {i} ")
    nii = nb.load(i)
    data = np.asarray(nii.dataobj)

    # Zoom factors for downsampling
    zoom_factor = 2

    # Downsample the image using nearest-neighbor interpolation
    data_new = zoom(data, zoom_factor, order=INTERPOLATION, mode='reflect')

    print("    Original shape  :", data.shape)
    print("    Resampled shape :", data_new.shape)

    # Prepare affine
    new_affine = np.copy(nii.affine)
    new_affine[0, 0] /= 2.
    new_affine[1, 1] /= 2.
    new_affine[2, 2] /= 2.
    new_affine[3, 3] /= 2.

    # Make a new nifti image
    nii_new = nb.Nifti1Image(data_new, affine=new_affine, header=nii.header)

    # Edit nifti header information
    nii_new.header["pixdim"][1] /= 2
    nii_new.header["pixdim"][2] /= 2
    nii_new.header["pixdim"][3] /= 2

    # Save nifti
    print("  Saving...")
    basename, ext = i.split(os.extsep, 1)
    basename = os.path.basename(basename)
    out_file = os.path.join(OUTDIR, "{}_resamp-0pt5.nii.gz".format(basename))
    nb.save(nii_new, out_file)

print('\n\nFinished.')
