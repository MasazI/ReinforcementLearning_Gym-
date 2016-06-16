#encoding: utf-8
import gym

# カートの上に棒がたってるもの
env = gym.make('CartPole-v0')
env.reset()

for _ in xrange(1000):
    env.render()

    # カートの上に棒がたってるもののアクション（サンプル）
    env.step(env.action_space.sample())
