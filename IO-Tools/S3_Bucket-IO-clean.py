'''
BOTO3 - Connecting to AWS S3 Buckets  with Python
    - Loose collection of code used to connect to S3 buckets on AWS
            - used to create client and resource sessions
            - comments contain resources for additional information
            - still a work in progress, some sections will be better defined
                than others

    - in[#] defines each cell, describes what code below it does
            - comments above will describe relevant information
            - including quick definitions, and reference guides

    - Treat the comments above in[#] as a loose set of instructions
            - code is not meant to be run as is
            - parts are meant to be combined to achieve specific tasks

    - This is best used when taking pieces of this to connect to S3 sessions


'''
# coding: utf-8

# ## AWS S3 Bucket term guide
# - **S3** - AWS Simple Storage Service - web scale computing, store and retrieve any data at any time. (https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)
# - **Buckets** -
# - **Objects** -
# - **Keys** -
# - **Regions** -
# - **Amazon S3 Data Consistency Model** -
# -

# ### Reference Guide
#
# - boto3 documentation
#     - API source doc - https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
#     - quickstart - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
#
# - Full Documentation
#     - S3 - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#id200
#     - All Services - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
#
# - Differences Client vs. Resource
#     - https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session

# In[1]:


# import library
import boto3


# set credentials
aws_access_key_id = ''
aws_secret_access_key = ''


# specify region to use
region='us-west-1'


# create session - M4 creds
session = boto3.Session(
    aws_access_key_id,    # access key ID
    aws_secret_access_key,    # secret access key
    region_name = region    # set region info
)


# resource session
s3 = session.resource('s3')


# ## Session Methods
#
# - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html

# ## Client Level Access

# In[1]:


client = session.client('s3')

client


# ## Resource Level Access
#
# - Guides
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html
#
# - Terms -
#     - Bucket - repository for objects to reference
#     - Object - key name identifies the object in a bucket, list of objects appear in the bucket
#     - Object keys - particular names assigned to objects in S3 bucket
#     - Object metadata - features/attributes of given object key/value pairs
#

# **Setting Resource Access S3 Bucket**

# In[2]:


s3 = session.resource('s3')


# **Print S3 Buckets available in Session-Resources**
#
# - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#using-boto-3

# In[3]:


for bucket in s3.buckets.all():
    print(bucket.name)


# **Open Specific S3 bucket by name**

# In[62]:


s3_name = ''

bucket = s3.Bucket(s3_name)

print(bucket)


# ## Bucket Operations

# **Uploading File**
# - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
#     - Uploading objects - upload objects up to 5GB in size, use multipart upload API if not
#     - Copying objects - can copy object up to 5GB in size for single operation, requires mutlipart upload API for others
#
# **Bucket operations**
# - https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectOperations.html

# In[99]:


for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)


# **Upload File - Then Print objects in bucket**

# In[79]:


# creates new bucket
fname = ''
key = 'PanelRetention-folder.zip'


# uploads
bucket.upload_file(
    Filename=str(fname),
    Key=str(key))


for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)


# **Downloading File**

# In[28]:


# import/output name & directories
fname = '/'
key = 'PanelRetention-Test.csv'

# download file method
bucket.download_file(
    Key=key,
    Filename='./PanelRetention-test.csv')

# print local file directory
import os    # import os library for pathing information

print('\t-- File Directory -- ')
print('')
for item in os.listdir():
    print(item)



# **Deleting File**

# In[89]:


# REQUIRES BEING IN A CURRENT WORKING S3 BUCKET

deleted_file = ''

bucket.Object(deleted_file).delete()


# ## Folder - Directory Management

# **Creating Buckets**

# In[93]:


client = session.client('s3')

fname = ''
source_bucket = ''
key_created = 'buckettest'

client.put_object(Bucket=source_bucket, Key=source_bucket)


# **Deleting Buckets**

# In[98]:


del_param = {'Objects':[{'Key':''}]}

bucket.delete_objects(Delete=del_param)
