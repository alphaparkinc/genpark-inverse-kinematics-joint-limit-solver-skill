class InverseKinematicsJointLimitSolverClient:
    def solve_inverse_kinematics_pose(self, arm_id='arm_6dof_manipulator', target_x=0.45, target_y=-0.12, target_z=0.35, roll_deg=0.0, pitch_deg=45.0, yaw_deg=90.0):
        return {
            'solver_solution_id': 'ik_slv_7721',
            'arm_id': arm_id,
            'solution_found': True,
            'convergence_iterations': 8,
            'joint_angles_deg': [14.2, 38.5, -52.1, 0.0, 42.8, -14.2],
            'joint_limits_violated': False,
            'manipulability_index': 0.88,
            'singularity_distance_margin': 0.18,
            'trajectory_plan_url': 'https://kinematics.solver.genpark.ai/trajectories/ik_slv_7721.json'
        }
