@principal_bp.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_submitted_assignments(p):
    """List all submitted assignments"""
    assignments = Assignment.get_all_submitted_assignments()
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)
    @principal_bp.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """List all teachers"""
    teachers = Teacher.get_all_teachers()  
    teachers_dump = TeacherSchema().dump(teachers, many=True) 
    return APIResponse.respond(data=teachers_dump)
@principal_bp.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade or re-grade an assignment"""
    grade_payload = AssignmentGradeSchema().load(incoming_payload)
    
    graded_assignment = Assignment.grade_or_regrade(
        _id=grade_payload.id,
        grade=grade_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
