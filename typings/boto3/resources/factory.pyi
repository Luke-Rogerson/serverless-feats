"""
This type stub file was generated by pyright.
"""

import logging

logger = logging.getLogger(__name__)
class ResourceFactory(object):
    """
    A factory to create new :py:class:`~boto3.resources.base.ServiceResource`
    classes from a :py:class:`~boto3.resources.model.ResourceModel`. There are
    two types of lookups that can be done: one on the service itself (e.g. an
    SQS resource) and another on models contained within the service (e.g. an
    SQS Queue resource).
    """
    def __init__(self, emitter) -> None:
        ...
    
    def load_from_definition(self, resource_name, single_resource_json_definition, service_context):
        """
        Loads a resource from a model, creating a new
        :py:class:`~boto3.resources.base.ServiceResource` subclass
        with the correct properties and methods, named based on the service
        and resource name, e.g. EC2.Instance.

        :type resource_name: string
        :param resource_name: Name of the resource to look up. For services,
                              this should match the ``service_name``.

        :type single_resource_json_definition: dict
        :param single_resource_json_definition:
            The loaded json of a single service resource or resource
            definition.

        :type service_context: :py:class:`~boto3.utils.ServiceContext`
        :param service_context: Context about the AWS service

        :rtype: Subclass of :py:class:`~boto3.resources.base.ServiceResource`
        :return: The service or resource class.
        """
        ...
    

