from client import InverseKinematicsJointLimitSolverClient

def main():
    client = InverseKinematicsJointLimitSolverClient()
    res = client.solve_inverse_kinematics_pose()
    print('IK Joint Limit Solver: ' + res['solver_solution_id'] + ' (Converged: ' + str(res['solution_found']) + ')')
    print('Joints (deg): ' + str(res['joint_angles_deg']) + ' | Manipulability: ' + str(res['manipulability_index']))
    print('Plan URL: ' + res['trajectory_plan_url'])

if __name__ == '__main__':
    main()
