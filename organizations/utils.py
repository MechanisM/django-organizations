from organizations.models import (Organization, OrganizationUser,
        OrganizationOwner)


def create_organization(user, name):
    """
    Returns a new organization, also creating an initial organization user who
    is the owner.
    """
    organization = Organization.objects.create(name=name)
    new_user = OrganizationUser.objects.create(organization=organization,
            user=user, is_admin=True)
    OrganizationOwner.objects.create(organization=organization,
            organization_user=new_user)
    return organization


def model_field_attr(model, field, attr):
    """
    Returns the specified attribute for the specified field on the model class.
    """
    fields = {field.name: field for field in model._meta.fields}
    return getattr(fields[field], attr)
