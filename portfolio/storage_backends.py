from storages.backends.s3boto3 import S3Boto3Storage


class ProjectImagesStorage(S3Boto3Storage):
    location = "project_images"
    file_overwrite = False


class CvStorage(S3Boto3Storage):
    location = "cv"
    file_overwrite = True
