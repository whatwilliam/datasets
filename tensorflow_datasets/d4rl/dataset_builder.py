# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Builder and Buidler Configs for D4RL Datasets."""

from typing import Any, Dict, FrozenSet

import dataclasses
import tensorflow.compat.v2 as tf
from tensorflow_datasets.d4rl import dataset_utils
import tensorflow_datasets.public_api as tfds


@dataclasses.dataclass
class BuilderConfig(tfds.core.BuilderConfig):
  dataset_dir: str = 'gym_mujoco'
  file_suffix: str = 'medium'
  # All use float32 except for the replay datasets.
  float_type: tf.DType = tf.float32
  # All datasets have step metadata except for mujoco v0.
  step_metadata_keys: FrozenSet[str] = frozenset([])
  episode_metadata_keys: FrozenSet[str] = frozenset([])
  has_policy_metadata: bool = False
  # Only used if the dataset has policy metadata
  has_policy_last_fc_log_std: bool = False
  policy_size: int = 256


@dataclasses.dataclass
class DatasetConfig():
  """Configuration of the shape of the dataset.

  Attributes:
    name: name of the Mujoco task
    obs_len: first dimension of the obsercations.
    action_len: first dimension of the actions.
    qpos_len: first dimension of the infos/qpos field (ignored if the dataset
      does not include step metadata).
    qvel_len: first dimension of the infos/qvel field (ignored if the dataset
      does not include step metadata).
  """
  name: str
  obs_len: int
  action_len: int
  qpos_len: int
  qvel_len: int


# pytype: disable=wrong-keyword-args
MUJOCO_BUILDER_CONFIGS = [
    BuilderConfig(
        name='v0-expert',
        dataset_dir='gym_mujoco',
        file_suffix='_expert',
        float_type=tf.float32,
        step_metadata_keys=set(),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-medium',
        dataset_dir='gym_mujoco',
        file_suffix='_medium',
        float_type=tf.float32,
        step_metadata_keys=set(),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-medium-expert',
        dataset_dir='gym_mujoco',
        file_suffix='_medium_expert',
        float_type=tf.float32,
        step_metadata_keys=set(),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-mixed',
        dataset_dir='gym_mujoco',
        file_suffix='_mixed',
        float_type=tf.float32,
        step_metadata_keys=set(),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-random',
        dataset_dir='gym_mujoco',
        file_suffix='_random',
        float_type=tf.float32,
        step_metadata_keys=set(),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-expert',
        dataset_dir='gym_mujoco_v1',
        file_suffix='_expert-v1',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(['algorithm', 'iteration']),
        has_policy_metadata=True,
        has_policy_last_fc_log_std=True,
        policy_size=256),
    BuilderConfig(
        name='v1-medium',
        dataset_dir='gym_mujoco_v1',
        file_suffix='_medium-v1',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(['algorithm', 'iteration']),
        has_policy_metadata=True,
        has_policy_last_fc_log_std=True,
        policy_size=256),
    BuilderConfig(
        name='v1-medium-expert',
        dataset_dir='gym_mujoco_v1',
        file_suffix='_medium_expert-v1',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-medium-replay',
        dataset_dir='gym_mujoco_v1',
        file_suffix='_medium_replay-v1',
        float_type=tf.float64,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(['algorithm', 'iteration']),
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-full-replay',
        dataset_dir='gym_mujoco_v1',
        file_suffix='_full_replay-v1',
        float_type=tf.float64,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(['algorithm', 'iteration']),
        has_policy_metadata=False,
        has_policy_last_fc_log_std=False),
    BuilderConfig(
        name='v1-random',
        dataset_dir='gym_mujoco_v1',
        file_suffix='_random-v1',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v2-expert',
        dataset_dir='gym_mujoco_v2',
        file_suffix='_expert-v2',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(['algorithm', 'iteration']),
        has_policy_metadata=True,
        has_policy_last_fc_log_std=True,
        policy_size=256),
    BuilderConfig(
        name='v2-full-replay',
        dataset_dir='gym_mujoco_v2',
        file_suffix='_full_replay-v2',
        float_type=tf.float64,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(['algorithm', 'iteration']),
        has_policy_metadata=False),
    BuilderConfig(
        name='v2-medium',
        dataset_dir='gym_mujoco_v2',
        file_suffix='_medium-v2',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(['algorithm', 'iteration']),
        has_policy_metadata=True,
        has_policy_last_fc_log_std=True,
        policy_size=256),
    BuilderConfig(
        name='v2-medium-expert',
        dataset_dir='gym_mujoco_v2',
        file_suffix='_medium_expert-v2',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v2-medium-replay',
        dataset_dir='gym_mujoco_v2',
        file_suffix='_medium_replay-v2',
        float_type=tf.float64,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(['algorithm', 'iteration']),
        has_policy_metadata=False),
    BuilderConfig(
        name='v2-random',
        dataset_dir='gym_mujoco_v2',
        file_suffix='_random-v2',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_log_probs']),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
]
ADROIT_BUILDER_CONFIGS = [
    BuilderConfig(
        name='v0-human',
        dataset_dir='hand_dapg',
        file_suffix='-v0_demos_clipped',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel']),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-cloned',
        dataset_dir='hand_dapg',
        file_suffix='-demos-v0-bc-combined',
        float_type=tf.float64,
        step_metadata_keys=set(['qpos', 'qvel']),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-expert',
        dataset_dir='hand_dapg',
        file_suffix='-v0_expert_clipped',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'action_mean',
                                'action_logstd']),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-human',
        dataset_dir='hand_dapg_v1',
        file_suffix='-human-v1',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'adroit_body_pos']),
        episode_metadata_keys=set(),
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-cloned',
        dataset_dir='hand_dapg_v1',
        file_suffix='-cloned-v1',
        float_type=tf.float32,
        step_metadata_keys=set(['qpos', 'qvel', 'adroit_body_pos']),
        episode_metadata_keys=set(['algorithm']),
        has_policy_metadata=True,
        has_policy_last_fc_log_std=False,
        policy_size=256,
    ),
    BuilderConfig(
        name='v1-expert',
        dataset_dir='hand_dapg_v1',
        file_suffix='-expert-v1',
        float_type=tf.float32,
        step_metadata_keys=set([
            'qpos', 'qvel', 'adroit_body_pos', 'action_mean', 'action_log_std'
        ]),
        episode_metadata_keys=set(['algorithm']),
        has_policy_metadata=True,
        has_policy_last_fc_log_std=True,
        policy_size=32,
    ),
]


def _get_step_metadata(
    builder_config: BuilderConfig,
    ds_config: DatasetConfig) -> Dict[str, tfds.features.FeatureConnector]:
  """Builds the features dict of the step metadata.

  Args:
    builder_config: builder config of the dataset.
    ds_config: config containing the dataset specs.

  Returns:
    Dictionary with the step metadata features of this dataset.
  """
  infos_dict = {}
  float_type = builder_config.float_type
  # Step metadata corresponds to state information.
  # See https://github.com/rail-berkeley/d4rl/wiki/Tasks#gym.
  for k in builder_config.step_metadata_keys:
    if k in 'action_log_probs':
      infos_dict[k] = float_type
    elif k == 'qpos':
      infos_dict[k] = tfds.features.Tensor(
          shape=(ds_config.qpos_len,), dtype=float_type)
    elif k == 'qvel':
      infos_dict[k] = tfds.features.Tensor(
          shape=(ds_config.qvel_len,), dtype=float_type)
    elif k == 'adroit_body_pos':
      if ds_config.name == 'door':
        adroit_key = {'door_body_pos'}
      elif ds_config.name == 'hammer':
        adroit_key = {'board_pos', 'target_pos'}
      else:
        raise ValueError(
            f'key {k} found in {ds_config.name} can only be present in Adroit datasets'
        )
      for ak in adroit_key:
        infos_dict[ak] = tfds.features.Tensor(shape=(3,), dtype=float_type)
    elif k in ['action_mean', 'action_log_std', 'action_logstd']:
      infos_dict[k] = tfds.features.Tensor(
          shape=(ds_config.action_len,), dtype=float_type)
    else:
      raise ValueError(f'Unknown key in the step metadata {k}')
  return infos_dict


def _get_policy_info(
    builder_config: BuilderConfig,
    ds_config: DatasetConfig) -> Dict[str, tfds.features.FeatureConnector]:
  """Builds the features dict of the policy weights.

  Args:
    builder_config: builder config of the dataset.
    ds_config: config containing the dataset specs.

  Returns:
    Dictionary with the policy-related features of this dataset.
  """
  float_type = builder_config.float_type
  # The policy dictionary contains the weights of the policy used to
  # generate the dataset.
  # See https://github.com/rail-berkeley/d4rl/wiki/Tasks#gym.
  policy_dict = {
      'fc0': {
          'bias':
              tfds.features.Tensor(
                  shape=(builder_config.policy_size,), dtype=float_type),
          'weight':
              tfds.features.Tensor(
                  shape=(builder_config.policy_size, ds_config.obs_len),
                  dtype=float_type),
      },
      'fc1': {
          'bias':
              tfds.features.Tensor(
                  shape=(builder_config.policy_size,), dtype=float_type),
          'weight':
              tfds.features.Tensor(
                  shape=(builder_config.policy_size,
                         builder_config.policy_size),
                  dtype=float_type),
      },
      'last_fc': {
          'bias':
              tfds.features.Tensor(
                  shape=(ds_config.action_len,), dtype=float_type),
          'weight':
              tfds.features.Tensor(
                  shape=(ds_config.action_len, builder_config.policy_size),
                  dtype=float_type),
      },
      'nonlinearity': tf.string,
      'output_distribution': tf.string,
  }
  if ds_config.name in ['door', 'hammer'
                       ] and builder_config.name == 'v1-cloned':
    # v1-cloned from d4rl_adroit uses a different policy shape
    policy_dict['fc0']['weight'] = tfds.features.Tensor(
        shape=(ds_config.obs_len, builder_config.policy_size), dtype=float_type)
    policy_dict['last_fc']['weight'] = tfds.features.Tensor(
        shape=(builder_config.policy_size, ds_config.action_len),
        dtype=float_type)
  if builder_config.has_policy_last_fc_log_std:
    policy_dict['last_fc_log_std'] = {
        'bias':
            tfds.features.Tensor(
                shape=(ds_config.action_len,), dtype=float_type),
        'weight':
            tfds.features.Tensor(
                shape=(ds_config.action_len, builder_config.policy_size),
                dtype=float_type),
    }

  return policy_dict


def get_features_dict(
    builder_config: BuilderConfig,
    ds_config: DatasetConfig) -> Dict[str, tfds.features.FeatureConnector]:
  """Builds the features dict of a D4RL dataset.

  Args:
    builder_config: builder config of the Mujoco dataset.
    ds_config: config of the Mujoco dataset containing the specs.

  Returns:
    Dictionary with the features of this dataset.
  """

  float_type = builder_config.float_type

  steps_dict = {
      'observation':
          tfds.features.Tensor(shape=(ds_config.obs_len,), dtype=float_type),
      'action':
          tfds.features.Tensor(shape=(ds_config.action_len,), dtype=float_type),
      'reward':
          float_type,
      'is_terminal':
          tf.bool,
      'is_first':
          tf.bool,
      'discount':
          float_type,
  }
  if ds_config.name in ['door', 'hammer'
                       ] and builder_config.name == 'v0-cloned':
    # In D4RL adroit door and hammer in the v0-cloned config, action uses a
    # different float type than the rest of the dataset.
    steps_dict['action'] = tfds.features.Tensor(
        shape=(ds_config.action_len,), dtype=tf.float32)

  if builder_config.step_metadata_keys:
    steps_dict['infos'] = _get_step_metadata(builder_config, ds_config)

  episode_metadata = {}
  if builder_config.episode_metadata_keys:
    for k in builder_config.episode_metadata_keys:
      if k == 'iteration':
        episode_metadata[k] = tf.int32
      else:
        episode_metadata[k] = tf.string
  if builder_config.has_policy_metadata:
    episode_metadata['policy'] = _get_policy_info(builder_config, ds_config)

  features_dict = {
      'steps': tfds.features.Dataset(steps_dict),
  }
  if episode_metadata:
    features_dict.update(episode_metadata)

  return features_dict


class D4RLDatasetBuilder(
    tfds.core.GeneratorBasedBuilder, skip_registration=True):
  """DatasetBuilder for D4RL datasets."""

  def __init__(self, *, ds_config: DatasetConfig, **kwargs: Any):
    self._ds_config = ds_config
    super().__init__(**kwargs)

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features_dict = get_features_dict(
        builder_config=self.builder_config, ds_config=self._ds_config)
    return tfds.core.DatasetInfo(
        builder=self,
        description=dataset_utils.description(),
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,  # disabled
        homepage=dataset_utils.url(),
        citation=dataset_utils.citation(),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    ds_dir = self.builder_config.dataset_dir
    name = self._ds_config.name
    if name == 'walker2d' and self.builder_config.name == 'v0-mixed':
      # There is a mismatch in the name of the original files, where one of them
      # uses walker instead of walker2d.
      name = 'walker'
    ds_name = (name + self.builder_config.file_suffix + '.hdf5')
    path = dl_manager.download_and_extract({
        'file_path':
            'http://rail.eecs.berkeley.edu/datasets/offline_rl/' + ds_dir +
            '/' + ds_name
    })
    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    file_path = path['file_path']
    return dataset_utils.generate_examples(file_path)
