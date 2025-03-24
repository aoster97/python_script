import numpy as np


# 定义目标函数（Rastrigin 函数）
def rastrigin(x, y):
    return 20 + x ** 2 + y ** 2 - 10 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))


# 粒子群优化（PSO）算法
def pso(num_particles=30, max_iter=1000, w=0.5, c1=1.5, c2=1.5):
    # 初始化粒子位置和速度
    particles = np.random.uniform(-5, 5, (num_particles, 2))  # 位置 (x, y)
    velocities = np.random.uniform(-1, 1, (num_particles, 2))  # 速度

    # 初始化个体最优和全局最优
    pbest = particles.copy()
    pbest_scores = np.array([rastrigin(p[0], p[1]) for p in particles])

    gbest = pbest[np.argmin(pbest_scores)]
    gbest_score = np.min(pbest_scores)

    # 迭代优化
    for i in range(max_iter):
        for j in range(num_particles):
            # 计算当前粒子的新目标值
            fitness = rastrigin(particles[j][0], particles[j][1])

            # 更新个体最优
            if fitness < pbest_scores[j]:
                pbest_scores[j] = fitness
                pbest[j] = particles[j].copy()

            # 更新全局最优
            if fitness < gbest_score:
                gbest_score = fitness
                gbest = particles[j].copy()

        # 更新粒子速度和位置
        r1, r2 = np.random.rand(num_particles, 1), np.random.rand(num_particles, 1)
        velocities = (w * velocities +
                      c1 * r1 * (pbest - particles) +
                      c2 * r2 * (gbest - particles))
        particles += velocities

        # 记录进度
        if i % 100 == 0:
            print(f"Iter {i}: Best Position = {gbest}, Best Score = {gbest_score:.4f}")

    return gbest, gbest_score


# 运行 PSO
best_position, best_value = pso()

print(f"\n最优解: x = {best_position[0]:.4f}, y = {best_position[1]:.4f}, f(x,y) = {best_value:.4f}")
