@principal_bp.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_submitted_assignments(p):
    """List all submitted assignments"""
    assignments = Assignment.get_all_submitted_assignments()
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)
