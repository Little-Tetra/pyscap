class _IdType:
    _type = None

    def __init__(self, namespace, content):
        """

        :param namespace:
        :type namespace: str
        :param content:
        :type content: str
        """
        self.namespace = namespace
        self.content = content

    def __str__(self):
        if self._type is None:
            raise NotImplementedError
        return f"xccdf_{self.namespace}_{self._type}_{self.content}"


class BenchmarkIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Benchmark> elements. xccdf_N_benchmark_S, where N is a
    reverse-DNS style namespace and S is an NCName-compatible string.
    """
    _type = "benchmark"


class RuleIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Rule> elements. xccdf_N_rule_S, where N is a reverse-DNS style
    namespace and S is an NCName-compatible string.
    """
    _type = "rule"


class GroupIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Group> elements. xccdf_N_group_S, where N is a reverse-DNS
    style namespace and S is an NCName-compatible string.
    """
    _type = "group"


class ValueIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Value> elements. xccdf_N_value_S, where N is a reverse-DNS
    style namespace and S is an NCName-compatible string.
    """
    _type = "value"


class ProfileIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Profile> elements. xccdf_N_profile_S, where N is a reverse-DNS
    style namespace and S is an NCName-compatible string.
    """
    _type = "profile"


class TestResultIdType(_IdType):
    """
    The format required for the @id property of <xccdf:TestResult> elements. xccdf_N_testresult_S, where N is a
    reverse-DNS style namespace and S is an NCName-compatible string.
    """
    _type = "testresult"


class TailoringIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Tailoring> elements. xccdf_N_tailoring_S, where N is a
    reverse-DNS style namespace and S is an NCName-compatible string.
    """
    _type = "tailoring"
