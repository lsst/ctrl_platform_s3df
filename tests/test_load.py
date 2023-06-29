
import os.path
import unittest

from lsst.ctrl.execute import envString
from lsst.ctrl.execute.allocationConfig import AllocationConfig
from lsst.ctrl.execute.condorConfig import CondorConfig

TESTDIR = os.path.abspath(os.path.dirname(__file__))


class S3DFSimpleTestCase(unittest.TestCase):
    """Test basic configuration reading."""

    def test_exec_config(self):
        exec_config_name = os.path.join(TESTDIR, os.pardir, "etc", "config", "execConfig.py")

        resolved_name = envString.resolve(exec_config_name)
        configuration = CondorConfig()
        configuration.load(resolved_name)
        self.assertEqual(configuration.platform.scheduler, "slurm")

    def test_allocation_config(self):
        slurm_config_name = os.path.join(TESTDIR, os.pardir, "etc", "config", "slurmConfig.py")

        resolved_name = envString.resolve(slurm_config_name)
        configuration = AllocationConfig()
        configuration.load(resolved_name)
        self.assertEqual(configuration.platform.queue, "$QUEUE")


if __name__ == "__main__":
    unittest.main()
