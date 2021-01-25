from enum import Enum


class CheckEnumeration(Enum):
    """The CheckEnumeration simple type defines acceptable check values, which
    are used to determine the final result of something based on the results of
    individual components.

    When used to define the relationship between objects and states,
    each check value defines how many of the matching objects (items
    except those with a status of does not exist) must satisfy the given
    state for the test to return true. When used to define the
    relationship between instances of a given entity, the different
    check values defines how many instances must be true for the entity
    to return true. When used to define the relationship between
    entities and multiple variable values, each check value defines how
    many variable values must be true for the entity to return true.

    :cvar ALL: A value of 'all' means that a final result of true is
        given if all the individual results under consideration are
        true.
    :cvar AT_LEAST_ONE: A value of 'at least one' means that a final
        result of true is given if at least one of the individual
        results under consideration is true.
    :cvar NONE_EXIST: A value of 'none exists' means that a test
        evaluates to true if no matching object exists that satisfy the
        data requirements.
    :cvar NONE_SATISFY: A value of 'none satisfy' means that a final
        result of true is given if none the individual results under
        consideration are true.
    :cvar ONLY_ONE: A value of 'only one' means that a final result of
        true is given if one and only one of the individual results
        under consideration are true.
    """
    ALL = "all"
    AT_LEAST_ONE = "at least one"
    NONE_EXIST = "none exist"
    NONE_SATISFY = "none satisfy"
    ONLY_ONE = "only one"


class ClassEnumeration(Enum):
    """The ClassEnumeration simple type defines the different classes of
    definitions.

    Each class defines a certain intent regarding how an OVAL Definition
    is written and what that definition is describing. The specified
    class gives a hint about the definition so a user can know what the
    definition writer is trying to say. Note that the class does not
    make a statement about whether a true result is good or bad as this
    depends on the use of an OVAL Definition. These classes are also
    used to group definitions by the type of system state they are
    describing. For example, this allows users to find all the
    vulnerability (or patch, or inventory, etc) definitions.

    :cvar COMPLIANCE: A compliance definition describes the state of a
        machine as it complies with a specific policy. A definition of
        this class will evaluate to true when the system is found to be
        compliant with the stated policy. Another way of thinking about
        this is that a compliance definition is stating "the system is
        compliant if ...".
    :cvar INVENTORY: An inventory definition describes whether a
        specific piece of software is installed on the system. A
        definition of this class will evaluate to true when the
        specified software is found on the system. Another way of
        thinking about this is that an inventory definition is stating
        "the software is installed if ...".
    :cvar MISCELLANEOUS: The 'miscellaneous' class is used to identify
        definitions that do not fall into any of the other defined
        classes.
    :cvar PATCH: A patch definition details the machine state of whether
        a patch executable should be installed. A definition of this
        class will evaluate to true when the specified patch is missing
        from the system. Another way of thinking about this is that a
        patch definition is stating "the patch should be installed if
        ...". Note that word SHOULD is intended to mean more than just
        CAN the patch executable be installed. In other words, if a more
        recent patch is already installed then the specified patch might
        not need to be installed.
    :cvar VULNERABILITY: A vulnerability definition describes the
        conditions under which a machine is vulnerable. A definition of
        this class will evaluate to true when the system is found to be
        vulnerable with the stated issue. Another way of thinking about
        this is that a vulnerability definition is stating "the system
        is vulnerable if ...".
    """
    COMPLIANCE = "compliance"
    INVENTORY = "inventory"
    MISCELLANEOUS = "miscellaneous"
    PATCH = "patch"
    VULNERABILITY = "vulnerability"


class ComplexDatatypeEnumeration(Enum):
    """The ComplexDatatypeEnumeration simple type defines the complex legal
    datatypes that are supported in OVAL.

    These datatype describe the values of individual entities where the
    entity has some complex structure beyond simple string like content.

    :cvar RECORD: The record datatype describes an entity with
        structured set of named fields and values as its content. The
        only allowed operation within OVAL for record values is
        'equals'. Note that the record datatype is not currently allowed
        when using variables.
    """
    RECORD = "record"


class DatatypeEnumeration(Enum):
    """The DatatypeEnumeration simple type defines the legal datatypes that are
    used to describe the values of individual entities.

    A value should be interpreted according to the specified type. This
    is most important during comparisons. For example, is '21' less than
    '123'? will evaluate to true if the datatypes are 'int', but will
    evaluate to 'false' if the datatypes are 'string'. Another example
    is applying the 'equal' operation to '1.0.0.0' and '1.0'. With
    datatype 'string' they are not equal, with datatype 'version' they
    are.

    :cvar BINARY: The binary datatype is used to represent hex-encoded
        data that is in raw (non-printable) form. This datatype conforms
        to the W3C Recommendation for binary data meaning that each
        binary octet is encoded as a character tuple, consisting of two
        hexadecimal digits {[0-9a-fA-F]} representing the octet code.
        Expected operations within OVAL for binary values are 'equals'
        and 'not equal'.
    :cvar BOOLEAN: The boolean datatype represents standard boolean
        data, either true or false.  This datatype conforms to the W3C
        Recommendation for boolean data meaning that the following
        literals are legal values: {true, false, 1, 0}.  Expected
        operations within OVAL for boolean values are 'equals' and 'not
        equal'.
    :cvar EVR_STRING: The evr_string datatype represents the epoch,
        version, and release fields as a single version string. It has
        the form "EPOCH:VERSION-RELEASE". Comparisons involving this
        datatype should follow the algorithm of librpm's rpmvercmp()
        function. Expected operations within OVAL for evr_string values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar DEBIAN_EVR_STRING: The debian_evr_string datatype represents
        the epoch, upstream_version, and debian_revision fields, for a
        Debian package, as a single version string. It has the form
        "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Comparisons involving
        this datatype should follow the algorithm outlined in Chapter 5
        of the "Debian Policy Manual"
        (https://www.debian.org/doc/debian-policy/ch-
        controlfields.html#s-f-Version). Note that a null epoch is
        equivalent to a value of '0'. An implementation of this is the
        cmpversions() function in dpkg's enquiry.c. Expected operations
        within OVAL for debian_evr_string values are 'equals', 'not
        equal', 'greater than', 'greater than or equal', 'less than',
        and 'less than or equal'.
    :cvar FILESET_REVISION: The fileset_revision datatype represents the
        version string related to filesets in HP-UX. An example would be
        'A.03.61.00'. For more information, see the HP-UX "Software
        Distributor Administration Guide"
        (http://h20000.www2.hp.com/bc/docs/support/SupportManual/c01919399/c01919399.pdf).
        Expected operations within OVAL for fileset_version values are
        'equals', 'not equal', 'greater than', 'greater than or equal',
        'less than', and 'less than or equal'.
    :cvar FLOAT_VALUE: The float datatype describes standard float data.
        This datatype conforms to the W3C Recommendation for float data
        meaning it is patterned after the IEEE single-precision 32-bit
        floating point type.  The format consists of a decimal followed,
        optionally, by the character 'E' or 'e', followed by an integer
        exponent.  The special values positive and negative infinity and
        not-a-number have are represented by INF, -INF and NaN,
        respectively.  Expected operations within OVAL for float values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar IOS_VERSION: The ios_version datatype describes Cisco IOS
        Train strings. These are in essence version strings for IOS.
        Please refer to Cisco's IOS Reference Guide for information on
        how to compare different Trains as they follow a very specific
        pattern. Expected operations within OVAL for ios_version values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar INT_VALUE: The int datatype describes standard integer data.
        This datatype conforms to the W3C Recommendation for integer
        data which follows the standard mathematical concept of the
        integer numbers.  (no decimal point and infinite range)
        Expected operations within OVAL for int values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', 'less than or equal', 'bitwise and', and 'bitwise or'.
    :cvar IPV4_ADDRESS: The ipv4_address datatype represents IPv4
        addresses and IPv4 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^32) (the representable range of a
        32-bit unsigned int), and the second is in the range [0,32]. The
        first element is an address, and the second is a prefix length.
        The lexical space is dotted-quad CIDR-like notation ('a.b.c.d'
        where 'a', 'b', 'c', and 'd' are integers from 0-255),
        optionally followed by a slash ('/') and either a prefix length
        (an integer from 0-32) or a netmask represented in the dotted-
        quad notation described previously. Examples of legal values are
        '192.0.2.0', '192.0.2.0/32', and '192.0.2.0/255.255.255.255'.
        Additionally, leading zeros are permitted such that '192.0.2.0'
        is equal to '192.000.002.000'. If a prefix length is not
        specified, it is implicitly equal to 32. The expected operations
        within OVAL for ipv4_address values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'subset of', and 'superset of'. All operations are
        defined in terms of the value space. Let A and B be ipv4_address
        values (i.e. ordered pairs from the value space). The following
        definitions assume that bits outside the prefix have been zeroed
        out. By zeroing the low order bits, they are effectively ignored
        for all operations. Implementations of the following operations
        MUST behave as if this has been done. The following defines how
        to perform each operation for the ipv4_address datatype. Let
        P_addr mean the first element of ordered pair P and P_prefix
        mean the second element. equals: A equals B if and only if
        A_addr == B_addr and A_prefix == B_prefix. not equal: A is not
        equal to B if and only if they don't satisfy the criteria for
        operator "equals". greater than: A is greater than B if and only
        if A_prefix == B_prefix and A_addr &gt; B_addr. If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. greater than or equal: A is greater than or equal to B
        if and only if A_prefix == B_prefix and they satisfy either the
        criteria for operators "equal" or "greater than". If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. less than: A is less than B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than or equal". If A_prefix != B_prefix, i.e. prefix
        lengths are not equal, an error MUST be reported. less than or
        equal: A is less than or equal to B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than". If A_prefix != B_prefix, i.e. prefix lengths are
        not equal, an error MUST be reported. subset of: A is a subset
        of B if and only if every IPv4 address in subnet A is present in
        subnet B. In other words, A_prefix &gt;= B_prefix and the high
        B_prefix bits of A_addr and B_addr are equal. superset of: A is
        a superset of B if and only if B is a subset of A.
    :cvar IPV6_ADDRESS: The ipv6_address datatype represents IPv6
        addresses and IPv6 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^128) (the representable range of
        a 128-bit unsigned int), and the second is in the range [0,128].
        The first element is an address, and the second is a prefix
        length. The lexical space is CIDR notation given in IETF
        specification RFC 4291 for textual representations of IPv6
        addresses and IPv6 address prefixes (see sections 2.2 and 2.3).
        If a prefix-length is not specified, it is implicitly equal to
        128. The expected operations within OVAL for ipv6_address values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', 'less than or equal', 'subset of', and
        'superset of'. All operations are defined in terms of the value
        space. Let A and B be ipv6_address values (i.e. ordered pairs
        from the value space). The following definitions assume that
        bits outside the prefix have been zeroed out. By zeroing the low
        order bits, they are effectively ignored for all operations.
        Implementations of the following operations MUST behave as if
        this has been done. The following defines how to perform each
        operation for the ipv6_address datatype. Let P_addr mean the
        first element of ordered pair P and P_prefix mean the second
        element. equals: A equals B if and only if A_addr == B_addr and
        A_prefix == B_prefix. not equal: A is not equal to B if and only
        if they don't satisfy the criteria for operator "equals".
        greater than: A is greater than B if and only if A_prefix ==
        B_prefix and A_addr &gt; B_addr. If A_prefix != B_prefix, an
        error MUST be reported. greater than or equal: A is greater than
        or equal to B if and only if A_prefix == B_prefix and they
        satisfy either the criteria for operators "equal" or "greater
        than". If A_prefix != B_prefix, an error MUST be reported. less
        than: A is less than B if and only if A_prefix == B_prefix and
        they don't satisfy the criteria for operator "greater than or
        equal". If A_prefix != B_prefix, an error MUST be reported. less
        than or equal: A is less than or equal to B if and only if
        A_prefix == B_prefix and they don't satisfy the criteria for
        operator "greater than". If A_prefix != B_prefix, an error MUST
        be reported. subset of: A is a subset of B if and only if every
        IPv6 address in subnet A is present in subnet B. In other words,
        A_prefix &gt;= B_prefix and the high B_prefix bits of A_addr and
        B_addr are equal. superset of: A is a superset of B if and only
        if B is a subset of A.
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar VERSION: The version datatype represents a value that is a
        hierarchical list of non-negative integers separated by a single
        character delimiter.  Note that any non-number character can be
        used as a delimiter and that different characters can be used
        within the same version string.  So '#.#-#' is the same as
        '#.#.#' or '#c#c#' where '#' is any non-negative integer.
        Expected operations within OVAL for version values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', and 'less than or equal'. For example '#.#.#' or
        '#-#-#-#' where the numbers to the left are more significant
        than the numbers to the right. When performing an 'equals'
        operation on a version datatype, you should first check the left
        most number for equality. If that fails, then the values are not
        equal. If it succeeds, then check the second left most number
        for equality. Continue checking the numbers from left to right
        until the last number has been checked. If, after testing all
        the previous numbers, the last number is equal then the two
        versions are equal. When performing other operations, such as
        'less than', 'less than or equal', 'greater than, or 'greater
        than or equal', similar logic as above is used. Start with the
        left most number and move from left to right. For each number,
        check if it is less than the number you are testing against. If
        it is, then the version in question is less than the version you
        are testing against. If the number is equal, then move to check
        the next number to the right. For example, to test if 5.7.23 is
        less than or equal to 5.8.0 you first compare 5 to 5. They are
        equal so you move on to compare 7 to 8. 7 is less than 8 so the
        entire test succeeds and 5.7.23 is 'less than or equal' to
        5.8.0. The difference between the 'less than' and 'less than or
        equal' operations is how the last number is handled. If the last
        number is reached, the check should use the given operation
        (either 'less than' and 'less than or equal') to test the
        number. For example, to test if 4.23.6 is greater than 4.23.6
        you first compare 4 to 4. They are equal so you move on to
        compare 23 to 23. They are equal so you move on to compare 6 to
        6. This is the last number in the version and since 6 is not
        greater than 6, the entire test fails and 4.23.6 is not greater
        than 4.23.6. Version strings with a different number of
        components shall be padded with zeros to make them the same
        size. For example, if the version strings '1.2.3' and '6.7.8.9'
        are being compared, then the short one should be padded to
        become '1.2.3.0'.
    :cvar RECORD: The record datatype describes an entity with
        structured set of named fields and values as its content. The
        only allowed operation within OVAL for record values is
        'equals'. Note that the record datatype is not currently allowed
        when using variables.
    """
    BINARY = "binary"
    BOOLEAN = "boolean"
    EVR_STRING = "evr_string"
    DEBIAN_EVR_STRING = "debian_evr_string"
    FILESET_REVISION = "fileset_revision"
    FLOAT_VALUE = "float"
    IOS_VERSION = "ios_version"
    INT_VALUE = "int"
    IPV4_ADDRESS = "ipv4_address"
    IPV6_ADDRESS = "ipv6_address"
    STRING = "string"
    VERSION = "version"
    RECORD = "record"


class ExistenceEnumeration(Enum):
    """The ExistenceEnumeration simple type defines acceptable existence
    values, which are used to determine a result based on the existence of
    individual components.

    The main use for this is for a test regarding the existence of
    objects on the system. Its secondary use is for a state regarding
    the existence of entities in corresponding items.

    :cvar ALL_EXIST: When used in the context of an OVAL state entity's
        check_existence attribute, a value of 'all_exist' means that
        every item entity for an object defined by the description
        exists on the system. When used in the context of an OVAL test's
        check_existence attribute, this value is equivalent to
        'at_least_one_exists' because non-existent items have no impact
        upon evaluation.
    :cvar ANY_EXIST: A value of 'any_exist' means that zero or more
        objects defined by the description exist on the system.
    :cvar AT_LEAST_ONE_EXISTS: A value of 'at_least_one_exists' means
        that at least one object defined by the description exists on
        the system.
    :cvar NONE_EXIST: A value of 'none_exist' means that none of the
        objects defined by the description exist on the system.
    :cvar ONLY_ONE_EXISTS: A value of 'only_one_exists' means that only
        one object defined by the description exists on the system.
    """
    ALL_EXIST = "all_exist"
    ANY_EXIST = "any_exist"
    AT_LEAST_ONE_EXISTS = "at_least_one_exists"
    NONE_EXIST = "none_exist"
    ONLY_ONE_EXISTS = "only_one_exists"


class FamilyEnumeration(Enum):
    """The FamilyEnumeration simple type is a listing of families that OVAL
    supports at this time.

    Since new family values can only be added with new version of the
    schema, the value of 'undefined' is to be used when the desired
    family is not available.  Note that use of the undefined family
    value does not target all families, rather it means that some family
    other than one of the defined values is targeted.

    :cvar ANDROID: The android value describes the Android mobile
        operating system.
    :cvar ASA: The asa value describes the Cisco ASA security devices.
    :cvar APPLE_IOS: The apple_ios value describes the iOS mobile
        operating system.
    :cvar CATOS: The catos value describes the Cisco CatOS operating
        system.
    :cvar IOS: The ios value describes the Cisco IOS operating system.
    :cvar IOSXE: The iosxe value describes the Cisco IOS XE operating
        system.
    :cvar JUNOS: The junos value describes the Juniper JunOS operating
        system.
    :cvar MACOS: The macos value describes the Mac operating system.
    :cvar PIXOS: The pixos value describes the Cisco PIX operating
        system.
    :cvar UNDEFINED: The undefined value is to be used when the desired
        family is not available.
    :cvar UNIX: The unix value describes the UNIX operating system.
    :cvar VMWARE_INFRASTRUCTURE: The vmware_infrastructure value
        describes VMWare Infrastructure.
    :cvar WINDOWS: The windows value describes the Microsoft Windows
        operating system.
    """
    ANDROID = "android"
    ASA = "asa"
    APPLE_IOS = "apple_ios"
    CATOS = "catos"
    IOS = "ios"
    IOSXE = "iosxe"
    JUNOS = "junos"
    MACOS = "macos"
    PIXOS = "pixos"
    UNDEFINED = "undefined"
    UNIX = "unix"
    VMWARE_INFRASTRUCTURE = "vmware_infrastructure"
    WINDOWS = "windows"


class MessageLevelEnumeration(Enum):
    """The MessageLevelEnumeration simple type defines the different levels
    associated with a message.

    There is no specific criteria about which messages get assigned
    which level. This is completely arbitrary and up to the content
    producer to decide what is an error message and what is a debug
    message.

    :cvar DEBUG: Debug messages should only be displayed by a tool when
        run in some sort of verbose mode.
    :cvar ERROR: Error messages should be recorded when there was an
        error that did not allow the collection of specific data.
    :cvar FATAL: A fatal message should be recorded when an error causes
        the failure of more than just a single piece of data.
    :cvar INFO: Info messages are used to pass useful information about
        the data collection to a user.
    :cvar WARNING: A warning message reports something that might not
        correct but information was still collected.
    """
    DEBUG = "debug"
    ERROR = "error"
    FATAL = "fatal"
    INFO = "info"
    WARNING = "warning"


class OperationEnumeration(Enum):
    """The OperationEnumeration simple type defines acceptable operations.

    Each operation defines how to compare entities against their actual
    values.

    :cvar EQUALS: The 'equals' operation returns true if the actual
        value on the system is equal to the stated entity.  When the
        specified datatype is a string, this results in a case-sensitive
        comparison.
    :cvar NOT_EQUAL: The 'not equal' operation returns true if the
        actual value on the system is not equal to the stated entity.
        When the specified datatype is a string, this results in a case-
        sensitive comparison.
    :cvar CASE_INSENSITIVE_EQUALS: The 'case insensitive equals'
        operation is meant for string data and returns true if the
        actual value on the system is equal (using a case insensitive
        comparison) to the stated entity.
    :cvar CASE_INSENSITIVE_NOT_EQUAL: The 'case insensitive not equal'
        operation is meant for string data and returns true if the
        actual value on the system is not equal (using a case
        insensitive comparison) to the stated entity.
    :cvar GREATER_THAN: The 'greater than' operation returns true if the
        actual value on the system is greater than the stated entity.
    :cvar LESS_THAN: The 'less than' operation returns true if the
        actual value on the system is less than the stated entity.
    :cvar GREATER_THAN_OR_EQUAL: The 'greater than or equal' operation
        returns true if the actual value on the system is greater than
        or equal to the stated entity.
    :cvar LESS_THAN_OR_EQUAL: The 'less than or equal' operation returns
        true if the actual value on the system is less than or equal to
        the stated entity.
    :cvar BITWISE_AND: The 'bitwise and' operation is used to determine
        if a specific bit is set. It returns true if performing a
        BITWISE AND with the binary representation of the stated entity
        against the binary representation of the actual value on the
        system results in a binary value that is equal to the binary
        representation of the stated entity. For example, assuming a
        datatype of 'int', if the actual integer value of the setting on
        your machine is 6 (same as 0110 in binary), then performing a
        'bitwise and' with the stated integer 4 (0100) returns 4 (0100).
        Since the result is the same as the state mask, then the test
        returns true. If the actual value on your machine is 1 (0001),
        then the 'bitwise and' with the stated integer 4 (0100) returns
        0 (0000). Since the result is not the same as the stated mask,
        then the test fails.
    :cvar BITWISE_OR: The 'bitwise or' operation is used to determine if
        a specific bit is not set. It returns true if performing a
        BITWISE OR with the binary representation of the stated entity
        against the binary representation of the actual value on the
        system results in a binary value that is equal to the binary
        representation of the stated entity. For example, assuming a
        datatype of 'int', if the actual integer value of the setting on
        your machine is 6 (same as 0110 in binary), then performing a
        'bitwise or' with the stated integer 14 (1110) returns 14
        (1110). Since the result is the same as the state mask, then the
        test returns true. If the actual value on your machine is 1
        (0001), then the 'bitwise or' with the stated integer 14 (1110)
        returns 15 (1111). Since the result is not the same as the
        stated mask, then the test fails.
    :cvar PATTERN_MATCH: The 'pattern match' operation allows an item to
        be tested against a regular expression. When used by an entity
        in an OVAL Object, the regular expression represents the unique
        set of matching items on the system.  OVAL supports a common
        subset of the regular expression character classes, operations,
        expressions and other lexical tokens defined within Perl 5's
        regular expression specification. For more information on the
        supported regular expression syntax in OVAL see:
        http://oval.mitre.org/language/about/re_support_5.6.html
    :cvar SUBSET_OF: The 'subset of' operation returns true if the
        actual set on the system is a subset of the set defined by the
        stated entity.
    :cvar SUPERSET_OF: The 'superset of' operation returns true if the
        actual set on the system is a superset of the set defined by the
        stated entity.
    """
    EQUALS = "equals"
    NOT_EQUAL = "not equal"
    CASE_INSENSITIVE_EQUALS = "case insensitive equals"
    CASE_INSENSITIVE_NOT_EQUAL = "case insensitive not equal"
    GREATER_THAN = "greater than"
    LESS_THAN = "less than"
    GREATER_THAN_OR_EQUAL = "greater than or equal"
    LESS_THAN_OR_EQUAL = "less than or equal"
    BITWISE_AND = "bitwise and"
    BITWISE_OR = "bitwise or"
    PATTERN_MATCH = "pattern match"
    SUBSET_OF = "subset of"
    SUPERSET_OF = "superset of"


class OperatorEnumeration(Enum):
    """The OperatorEnumeration simple type defines acceptable operators.

    Each operator defines how to evaluate multiple arguments.

    :cvar AND_VALUE: The AND operator produces a true result if every
        argument is true. If one or more arguments are false, the result
        of the AND is false. If one or more of the arguments are
        unknown, and if none of the arguments are false, then the AND
        operator produces a result of unknown.
    :cvar ONE: The ONE operator produces a true result if one and only
        one argument is true. If there are more than argument is true
        (or if there are no true arguments), the result of the ONE is
        false. If one or more of the arguments are unknown, then the ONE
        operator produces a result of unknown.
    :cvar OR_VALUE: The OR operator produces a true result if one or
        more arguments is true. If every argument is false, the result
        of the OR is false. If one or more of the arguments are unknown
        and if none of arguments are true, then the OR operator produces
        a result of unknown.
    :cvar XOR: XOR is defined to be true if an odd number of its
        arguments are true, and false otherwise. If any of the arguments
        are unknown, then the XOR operator produces a result of unknown.
    """
    AND_VALUE = "AND"
    ONE = "ONE"
    OR_VALUE = "OR"
    XOR = "XOR"


class SimpleDatatypeEnumeration(Enum):
    """The SimpleDatatypeEnumeration simple type defines the legal datatypes
    that are used to describe the values of individual entities that can be
    represented in a XML string field.

    The value may have structure and a pattern, but it is represented as
    string content.

    :cvar BINARY: The binary datatype is used to represent hex-encoded
        data that is in raw (non-printable) form. This datatype conforms
        to the W3C Recommendation for binary data meaning that each
        binary octet is encoded as a character tuple, consisting of two
        hexadecimal digits {[0-9a-fA-F]} representing the octet code.
        Expected operations within OVAL for binary values are 'equals'
        and 'not equal'.
    :cvar BOOLEAN: The boolean datatype represents standard boolean
        data, either true or false.  This datatype conforms to the W3C
        Recommendation for boolean data meaning that the following
        literals are legal values: {true, false, 1, 0}.  Expected
        operations within OVAL for boolean values are 'equals' and 'not
        equal'.
    :cvar EVR_STRING: The evr_string datatype represents the epoch,
        version, and release fields as a single version string. It has
        the form "EPOCH:VERSION-RELEASE". Comparisons involving this
        datatype should follow the algorithm of librpm's rpmvercmp()
        function. Expected operations within OVAL for evr_string values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar DEBIAN_EVR_STRING: The debian_evr_string datatype represents
        the epoch, upstream_version, and debian_revision fields, for a
        Debian package, as a single version string. It has the form
        "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Comparisons involving
        this datatype should follow the algorithm outlined in Chapter 5
        of the "Debian Policy Manual"
        (https://www.debian.org/doc/debian-policy/ch-
        controlfields.html#s-f-Version). Note that a null epoch is
        equivalent to a value of '0'. An implementation of this is the
        cmpversions() function in dpkg's enquiry.c. Expected operations
        within OVAL for debian_evr_string values are 'equals', 'not
        equal', 'greater than', 'greater than or equal', 'less than',
        and 'less than or equal'.
    :cvar FILESET_REVISION: The fileset_revision datatype represents the
        version string related to filesets in HP-UX. An example would be
        'A.03.61.00'. For more information, see the HP-UX "Software
        Distributor Administration Guide"
        (http://h20000.www2.hp.com/bc/docs/support/SupportManual/c01919399/c01919399.pdf).
        Expected operations within OVAL for fileset_version values are
        'equals', 'not equal', 'greater than', 'greater than or equal',
        'less than', and 'less than or equal'.
    :cvar FLOAT_VALUE: The float datatype describes standard float data.
        This datatype conforms to the W3C Recommendation for float data
        meaning it is patterned after the IEEE single-precision 32-bit
        floating point type.  The format consists of a decimal followed,
        optionally, by the character 'E' or 'e', followed by an integer
        exponent.  The special values positive and negative infinity and
        not-a-number have are represented by INF, -INF and NaN,
        respectively.  Expected operations within OVAL for float values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar IOS_VERSION: The ios_version datatype describes Cisco IOS
        Train strings. These are in essence version strings for IOS.
        Please refer to Cisco's IOS Reference Guide for information on
        how to compare different Trains as they follow a very specific
        pattern. Expected operations within OVAL for ios_version values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar INT_VALUE: The int datatype describes standard integer data.
        This datatype conforms to the W3C Recommendation for integer
        data which follows the standard mathematical concept of the
        integer numbers.  (no decimal point and infinite range)
        Expected operations within OVAL for int values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', 'less than or equal', 'bitwise and', and 'bitwise or'.
    :cvar IPV4_ADDRESS: The ipv4_address datatype represents IPv4
        addresses and IPv4 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^32) (the representable range of a
        32-bit unsigned int), and the second is in the range [0,32]. The
        first element is an address, and the second is a prefix length.
        The lexical space is dotted-quad CIDR-like notation ('a.b.c.d'
        where 'a', 'b', 'c', and 'd' are integers from 0-255),
        optionally followed by a slash ('/') and either a prefix length
        (an integer from 0-32) or a netmask represented in the dotted-
        quad notation described previously. Examples of legal values are
        '192.0.2.0', '192.0.2.0/32', and '192.0.2.0/255.255.255.255'.
        Additionally, leading zeros are permitted such that '192.0.2.0'
        is equal to '192.000.002.000'. If a prefix length is not
        specified, it is implicitly equal to 32. The expected operations
        within OVAL for ipv4_address values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'subset of', and 'superset of'. All operations are
        defined in terms of the value space. Let A and B be ipv4_address
        values (i.e. ordered pairs from the value space). The following
        definitions assume that bits outside the prefix have been zeroed
        out. By zeroing the low order bits, they are effectively ignored
        for all operations. Implementations of the following operations
        MUST behave as if this has been done. The following defines how
        to perform each operation for the ipv4_address datatype. Let
        P_addr mean the first element of ordered pair P and P_prefix
        mean the second element. equals: A equals B if and only if
        A_addr == B_addr and A_prefix == B_prefix. not equal: A is not
        equal to B if and only if they don't satisfy the criteria for
        operator "equals". greater than: A is greater than B if and only
        if A_prefix == B_prefix and A_addr &gt; B_addr. If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. greater than or equal: A is greater than or equal to B
        if and only if A_prefix == B_prefix and they satisfy either the
        criteria for operators "equal" or "greater than". If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. less than: A is less than B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than or equal". If A_prefix != B_prefix, i.e. prefix
        lengths are not equal, an error MUST be reported. less than or
        equal: A is less than or equal to B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than". If A_prefix != B_prefix, i.e. prefix lengths are
        not equal, an error MUST be reported. subset of: A is a subset
        of B if and only if every IPv4 address in subnet A is present in
        subnet B. In other words, A_prefix &gt;= B_prefix and the high
        B_prefix bits of A_addr and B_addr are equal. superset of: A is
        a superset of B if and only if B is a subset of A.
    :cvar IPV6_ADDRESS: The ipv6_address datatype represents IPv6
        addresses and IPv6 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^128) (the representable range of
        a 128-bit unsigned int), and the second is in the range [0,128].
        The first element is an address, and the second is a prefix
        length. The lexical space is CIDR notation given in IETF
        specification RFC 4291 for textual representations of IPv6
        addresses and IPv6 address prefixes (see sections 2.2 and 2.3).
        If a prefix-length is not specified, it is implicitly equal to
        128. The expected operations within OVAL for ipv6_address values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', 'less than or equal', 'subset of', and
        'superset of'. All operations are defined in terms of the value
        space. Let A and B be ipv6_address values (i.e. ordered pairs
        from the value space). The following definitions assume that
        bits outside the prefix have been zeroed out. By zeroing the low
        order bits, they are effectively ignored for all operations.
        Implementations of the following operations MUST behave as if
        this has been done. The following defines how to perform each
        operation for the ipv6_address datatype. Let P_addr mean the
        first element of ordered pair P and P_prefix mean the second
        element. equals: A equals B if and only if A_addr == B_addr and
        A_prefix == B_prefix. not equal: A is not equal to B if and only
        if they don't satisfy the criteria for operator "equals".
        greater than: A is greater than B if and only if A_prefix ==
        B_prefix and A_addr &gt; B_addr. If A_prefix != B_prefix, an
        error MUST be reported. greater than or equal: A is greater than
        or equal to B if and only if A_prefix == B_prefix and they
        satisfy either the criteria for operators "equal" or "greater
        than". If A_prefix != B_prefix, an error MUST be reported. less
        than: A is less than B if and only if A_prefix == B_prefix and
        they don't satisfy the criteria for operator "greater than or
        equal". If A_prefix != B_prefix, an error MUST be reported. less
        than or equal: A is less than or equal to B if and only if
        A_prefix == B_prefix and they don't satisfy the criteria for
        operator "greater than". If A_prefix != B_prefix, an error MUST
        be reported. subset of: A is a subset of B if and only if every
        IPv6 address in subnet A is present in subnet B. In other words,
        A_prefix &gt;= B_prefix and the high B_prefix bits of A_addr and
        B_addr are equal. superset of: A is a superset of B if and only
        if B is a subset of A.
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    :cvar VERSION: The version datatype represents a value that is a
        hierarchical list of non-negative integers separated by a single
        character delimiter.  Note that any non-number character can be
        used as a delimiter and that different characters can be used
        within the same version string.  So '#.#-#' is the same as
        '#.#.#' or '#c#c#' where '#' is any non-negative integer.
        Expected operations within OVAL for version values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', and 'less than or equal'. For example '#.#.#' or
        '#-#-#-#' where the numbers to the left are more significant
        than the numbers to the right. When performing an 'equals'
        operation on a version datatype, you should first check the left
        most number for equality. If that fails, then the values are not
        equal. If it succeeds, then check the second left most number
        for equality. Continue checking the numbers from left to right
        until the last number has been checked. If, after testing all
        the previous numbers, the last number is equal then the two
        versions are equal. When performing other operations, such as
        'less than', 'less than or equal', 'greater than, or 'greater
        than or equal', similar logic as above is used. Start with the
        left most number and move from left to right. For each number,
        check if it is less than the number you are testing against. If
        it is, then the version in question is less than the version you
        are testing against. If the number is equal, then move to check
        the next number to the right. For example, to test if 5.7.23 is
        less than or equal to 5.8.0 you first compare 5 to 5. They are
        equal so you move on to compare 7 to 8. 7 is less than 8 so the
        entire test succeeds and 5.7.23 is 'less than or equal' to
        5.8.0. The difference between the 'less than' and 'less than or
        equal' operations is how the last number is handled. If the last
        number is reached, the check should use the given operation
        (either 'less than' and 'less than or equal') to test the
        number. For example, to test if 4.23.6 is greater than 4.23.6
        you first compare 4 to 4. They are equal so you move on to
        compare 23 to 23. They are equal so you move on to compare 6 to
        6. This is the last number in the version and since 6 is not
        greater than 6, the entire test fails and 4.23.6 is not greater
        than 4.23.6. Version strings with a different number of
        components shall be padded with zeros to make them the same
        size. For example, if the version strings '1.2.3' and '6.7.8.9'
        are being compared, then the short one should be padded to
        become '1.2.3.0'.
    """
    BINARY = "binary"
    BOOLEAN = "boolean"
    EVR_STRING = "evr_string"
    DEBIAN_EVR_STRING = "debian_evr_string"
    FILESET_REVISION = "fileset_revision"
    FLOAT_VALUE = "float"
    IOS_VERSION = "ios_version"
    INT_VALUE = "int"
    IPV4_ADDRESS = "ipv4_address"
    IPV6_ADDRESS = "ipv6_address"
    STRING = "string"
    VERSION = "version"


class ArithmeticEnumeration(Enum):
    """The ArithmeticEnumeration simple type defines basic arithmetic
    operations.

    Currently add and multiply are defined.
    """
    ADD = "add"
    MULTIPLY = "multiply"


class DateTimeFormatEnumeration(Enum):
    """The DateTimeFormatEnumeration simple type defines the different date-
    time formats that are understood by OVAL.

    Note that in some cases there are a few different possibilities
    within a given format. Each of these possibilities is unique though
    and can be distinguished from each other. The different formats are
    used to clarify the higher level structure of the date-time string
    being used.

    :cvar YEAR_MONTH_DAY: The year_month_day value specifies date-time
        strings that follow the formats: 'yyyymmdd', 'yyyymmddThhmmss',
        'yyyy/mm/dd hh:mm:ss', 'yyyy/mm/dd', 'yyyy-mm-dd hh:mm:ss', or
        'yyyy-mm-dd'
    :cvar MONTH_DAY_YEAR: The month_day_year value specifies date-time
        strings that follow the formats: 'mm/dd/yyyy hh:mm:ss',
        'mm/dd/yyyy', 'mm-dd-yyyy hh:mm:ss', 'mm-dd-yyyy', 'NameOfMonth,
        dd yyyy hh:mm:ss' or 'NameOfMonth, dd yyyy',
        'AbreviatedNameOfMonth, dd yyyy hh:mm:ss', or
        'AbreviatedNameOfMonth, dd yyyy'
    :cvar DAY_MONTH_YEAR: The day_month_year value specifies date-time
        strings that follow the formats: 'dd/mm/yyyy hh:mm:ss',
        'dd/mm/yyyy', 'dd-mm-yyyy hh:mm:ss', or 'dd-mm-yyyy'
    :cvar WIN_FILETIME: The win_filetime value specifies date-time
        strings that follow the windows file time format.
    :cvar SECONDS_SINCE_EPOCH: The seconds_since_epoch value specifies
        date-time values that represent the time in seconds since the
        UNIX epoch.  The Unix epoch is the time 00:00:00 UTC on January
        1, 1970.
    :cvar CIM_DATETIME: The cim_datetime model is used by WMI and its
        value specifies date-time strings that follow the format:
        'yyyymmddHHMMSS.mmmmmmsUUU', and alternatively 'yyyy-mm-dd
        HH:MM:SS:mmm' only when used in WMI Query Language queries.
    """
    YEAR_MONTH_DAY = "year_month_day"
    MONTH_DAY_YEAR = "month_day_year"
    DAY_MONTH_YEAR = "day_month_year"
    WIN_FILETIME = "win_filetime"
    SECONDS_SINCE_EPOCH = "seconds_since_epoch"
    CIM_DATETIME = "cim_datetime"


class EntityObjectIpaddressStringTypeDatatype(Enum):
    """
    :cvar BINARY: The binary datatype is used to represent hex-encoded
        data that is in raw (non-printable) form. This datatype conforms
        to the W3C Recommendation for binary data meaning that each
        binary octet is encoded as a character tuple, consisting of two
        hexadecimal digits {[0-9a-fA-F]} representing the octet code.
        Expected operations within OVAL for binary values are 'equals'
        and 'not equal'.
    :cvar BOOLEAN: The boolean datatype represents standard boolean
        data, either true or false.  This datatype conforms to the W3C
        Recommendation for boolean data meaning that the following
        literals are legal values: {true, false, 1, 0}.  Expected
        operations within OVAL for boolean values are 'equals' and 'not
        equal'.
    :cvar EVR_STRING: The evr_string datatype represents the epoch,
        version, and release fields as a single version string. It has
        the form "EPOCH:VERSION-RELEASE". Comparisons involving this
        datatype should follow the algorithm of librpm's rpmvercmp()
        function. Expected operations within OVAL for evr_string values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar DEBIAN_EVR_STRING: The debian_evr_string datatype represents
        the epoch, upstream_version, and debian_revision fields, for a
        Debian package, as a single version string. It has the form
        "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Comparisons involving
        this datatype should follow the algorithm outlined in Chapter 5
        of the "Debian Policy Manual"
        (https://www.debian.org/doc/debian-policy/ch-
        controlfields.html#s-f-Version). Note that a null epoch is
        equivalent to a value of '0'. An implementation of this is the
        cmpversions() function in dpkg's enquiry.c. Expected operations
        within OVAL for debian_evr_string values are 'equals', 'not
        equal', 'greater than', 'greater than or equal', 'less than',
        and 'less than or equal'.
    :cvar FILESET_REVISION: The fileset_revision datatype represents the
        version string related to filesets in HP-UX. An example would be
        'A.03.61.00'. For more information, see the HP-UX "Software
        Distributor Administration Guide"
        (http://h20000.www2.hp.com/bc/docs/support/SupportManual/c01919399/c01919399.pdf).
        Expected operations within OVAL for fileset_version values are
        'equals', 'not equal', 'greater than', 'greater than or equal',
        'less than', and 'less than or equal'.
    :cvar FLOAT_VALUE: The float datatype describes standard float data.
        This datatype conforms to the W3C Recommendation for float data
        meaning it is patterned after the IEEE single-precision 32-bit
        floating point type.  The format consists of a decimal followed,
        optionally, by the character 'E' or 'e', followed by an integer
        exponent.  The special values positive and negative infinity and
        not-a-number have are represented by INF, -INF and NaN,
        respectively.  Expected operations within OVAL for float values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar IOS_VERSION: The ios_version datatype describes Cisco IOS
        Train strings. These are in essence version strings for IOS.
        Please refer to Cisco's IOS Reference Guide for information on
        how to compare different Trains as they follow a very specific
        pattern. Expected operations within OVAL for ios_version values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar INT_VALUE: The int datatype describes standard integer data.
        This datatype conforms to the W3C Recommendation for integer
        data which follows the standard mathematical concept of the
        integer numbers.  (no decimal point and infinite range)
        Expected operations within OVAL for int values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', 'less than or equal', 'bitwise and', and 'bitwise or'.
    :cvar IPV4_ADDRESS:
    :cvar IPV6_ADDRESS:
    :cvar STRING:
    :cvar VERSION: The version datatype represents a value that is a
        hierarchical list of non-negative integers separated by a single
        character delimiter.  Note that any non-number character can be
        used as a delimiter and that different characters can be used
        within the same version string.  So '#.#-#' is the same as
        '#.#.#' or '#c#c#' where '#' is any non-negative integer.
        Expected operations within OVAL for version values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', and 'less than or equal'. For example '#.#.#' or
        '#-#-#-#' where the numbers to the left are more significant
        than the numbers to the right. When performing an 'equals'
        operation on a version datatype, you should first check the left
        most number for equality. If that fails, then the values are not
        equal. If it succeeds, then check the second left most number
        for equality. Continue checking the numbers from left to right
        until the last number has been checked. If, after testing all
        the previous numbers, the last number is equal then the two
        versions are equal. When performing other operations, such as
        'less than', 'less than or equal', 'greater than, or 'greater
        than or equal', similar logic as above is used. Start with the
        left most number and move from left to right. For each number,
        check if it is less than the number you are testing against. If
        it is, then the version in question is less than the version you
        are testing against. If the number is equal, then move to check
        the next number to the right. For example, to test if 5.7.23 is
        less than or equal to 5.8.0 you first compare 5 to 5. They are
        equal so you move on to compare 7 to 8. 7 is less than 8 so the
        entire test succeeds and 5.7.23 is 'less than or equal' to
        5.8.0. The difference between the 'less than' and 'less than or
        equal' operations is how the last number is handled. If the last
        number is reached, the check should use the given operation
        (either 'less than' and 'less than or equal') to test the
        number. For example, to test if 4.23.6 is greater than 4.23.6
        you first compare 4 to 4. They are equal so you move on to
        compare 23 to 23. They are equal so you move on to compare 6 to
        6. This is the last number in the version and since 6 is not
        greater than 6, the entire test fails and 4.23.6 is not greater
        than 4.23.6. Version strings with a different number of
        components shall be padded with zeros to make them the same
        size. For example, if the version strings '1.2.3' and '6.7.8.9'
        are being compared, then the short one should be padded to
        become '1.2.3.0'.
    """
    BINARY = "binary"
    BOOLEAN = "boolean"
    EVR_STRING = "evr_string"
    DEBIAN_EVR_STRING = "debian_evr_string"
    FILESET_REVISION = "fileset_revision"
    FLOAT_VALUE = "float"
    IOS_VERSION = "ios_version"
    INT_VALUE = "int"
    IPV4_ADDRESS = "ipv4_address"
    IPV6_ADDRESS = "ipv6_address"
    STRING = "string"
    VERSION = "version"


class EntityStateIosversionTypeDatatype(Enum):
    """
    :cvar BINARY: The binary datatype is used to represent hex-encoded
        data that is in raw (non-printable) form. This datatype conforms
        to the W3C Recommendation for binary data meaning that each
        binary octet is encoded as a character tuple, consisting of two
        hexadecimal digits {[0-9a-fA-F]} representing the octet code.
        Expected operations within OVAL for binary values are 'equals'
        and 'not equal'.
    :cvar BOOLEAN: The boolean datatype represents standard boolean
        data, either true or false.  This datatype conforms to the W3C
        Recommendation for boolean data meaning that the following
        literals are legal values: {true, false, 1, 0}.  Expected
        operations within OVAL for boolean values are 'equals' and 'not
        equal'.
    :cvar EVR_STRING: The evr_string datatype represents the epoch,
        version, and release fields as a single version string. It has
        the form "EPOCH:VERSION-RELEASE". Comparisons involving this
        datatype should follow the algorithm of librpm's rpmvercmp()
        function. Expected operations within OVAL for evr_string values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar DEBIAN_EVR_STRING: The debian_evr_string datatype represents
        the epoch, upstream_version, and debian_revision fields, for a
        Debian package, as a single version string. It has the form
        "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Comparisons involving
        this datatype should follow the algorithm outlined in Chapter 5
        of the "Debian Policy Manual"
        (https://www.debian.org/doc/debian-policy/ch-
        controlfields.html#s-f-Version). Note that a null epoch is
        equivalent to a value of '0'. An implementation of this is the
        cmpversions() function in dpkg's enquiry.c. Expected operations
        within OVAL for debian_evr_string values are 'equals', 'not
        equal', 'greater than', 'greater than or equal', 'less than',
        and 'less than or equal'.
    :cvar FILESET_REVISION: The fileset_revision datatype represents the
        version string related to filesets in HP-UX. An example would be
        'A.03.61.00'. For more information, see the HP-UX "Software
        Distributor Administration Guide"
        (http://h20000.www2.hp.com/bc/docs/support/SupportManual/c01919399/c01919399.pdf).
        Expected operations within OVAL for fileset_version values are
        'equals', 'not equal', 'greater than', 'greater than or equal',
        'less than', and 'less than or equal'.
    :cvar FLOAT_VALUE: The float datatype describes standard float data.
        This datatype conforms to the W3C Recommendation for float data
        meaning it is patterned after the IEEE single-precision 32-bit
        floating point type.  The format consists of a decimal followed,
        optionally, by the character 'E' or 'e', followed by an integer
        exponent.  The special values positive and negative infinity and
        not-a-number have are represented by INF, -INF and NaN,
        respectively.  Expected operations within OVAL for float values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar IOS_VERSION:
    :cvar INT_VALUE: The int datatype describes standard integer data.
        This datatype conforms to the W3C Recommendation for integer
        data which follows the standard mathematical concept of the
        integer numbers.  (no decimal point and infinite range)
        Expected operations within OVAL for int values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', 'less than or equal', 'bitwise and', and 'bitwise or'.
    :cvar IPV4_ADDRESS: The ipv4_address datatype represents IPv4
        addresses and IPv4 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^32) (the representable range of a
        32-bit unsigned int), and the second is in the range [0,32]. The
        first element is an address, and the second is a prefix length.
        The lexical space is dotted-quad CIDR-like notation ('a.b.c.d'
        where 'a', 'b', 'c', and 'd' are integers from 0-255),
        optionally followed by a slash ('/') and either a prefix length
        (an integer from 0-32) or a netmask represented in the dotted-
        quad notation described previously. Examples of legal values are
        '192.0.2.0', '192.0.2.0/32', and '192.0.2.0/255.255.255.255'.
        Additionally, leading zeros are permitted such that '192.0.2.0'
        is equal to '192.000.002.000'. If a prefix length is not
        specified, it is implicitly equal to 32. The expected operations
        within OVAL for ipv4_address values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'subset of', and 'superset of'. All operations are
        defined in terms of the value space. Let A and B be ipv4_address
        values (i.e. ordered pairs from the value space). The following
        definitions assume that bits outside the prefix have been zeroed
        out. By zeroing the low order bits, they are effectively ignored
        for all operations. Implementations of the following operations
        MUST behave as if this has been done. The following defines how
        to perform each operation for the ipv4_address datatype. Let
        P_addr mean the first element of ordered pair P and P_prefix
        mean the second element. equals: A equals B if and only if
        A_addr == B_addr and A_prefix == B_prefix. not equal: A is not
        equal to B if and only if they don't satisfy the criteria for
        operator "equals". greater than: A is greater than B if and only
        if A_prefix == B_prefix and A_addr &gt; B_addr. If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. greater than or equal: A is greater than or equal to B
        if and only if A_prefix == B_prefix and they satisfy either the
        criteria for operators "equal" or "greater than". If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. less than: A is less than B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than or equal". If A_prefix != B_prefix, i.e. prefix
        lengths are not equal, an error MUST be reported. less than or
        equal: A is less than or equal to B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than". If A_prefix != B_prefix, i.e. prefix lengths are
        not equal, an error MUST be reported. subset of: A is a subset
        of B if and only if every IPv4 address in subnet A is present in
        subnet B. In other words, A_prefix &gt;= B_prefix and the high
        B_prefix bits of A_addr and B_addr are equal. superset of: A is
        a superset of B if and only if B is a subset of A.
    :cvar IPV6_ADDRESS: The ipv6_address datatype represents IPv6
        addresses and IPv6 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^128) (the representable range of
        a 128-bit unsigned int), and the second is in the range [0,128].
        The first element is an address, and the second is a prefix
        length. The lexical space is CIDR notation given in IETF
        specification RFC 4291 for textual representations of IPv6
        addresses and IPv6 address prefixes (see sections 2.2 and 2.3).
        If a prefix-length is not specified, it is implicitly equal to
        128. The expected operations within OVAL for ipv6_address values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', 'less than or equal', 'subset of', and
        'superset of'. All operations are defined in terms of the value
        space. Let A and B be ipv6_address values (i.e. ordered pairs
        from the value space). The following definitions assume that
        bits outside the prefix have been zeroed out. By zeroing the low
        order bits, they are effectively ignored for all operations.
        Implementations of the following operations MUST behave as if
        this has been done. The following defines how to perform each
        operation for the ipv6_address datatype. Let P_addr mean the
        first element of ordered pair P and P_prefix mean the second
        element. equals: A equals B if and only if A_addr == B_addr and
        A_prefix == B_prefix. not equal: A is not equal to B if and only
        if they don't satisfy the criteria for operator "equals".
        greater than: A is greater than B if and only if A_prefix ==
        B_prefix and A_addr &gt; B_addr. If A_prefix != B_prefix, an
        error MUST be reported. greater than or equal: A is greater than
        or equal to B if and only if A_prefix == B_prefix and they
        satisfy either the criteria for operators "equal" or "greater
        than". If A_prefix != B_prefix, an error MUST be reported. less
        than: A is less than B if and only if A_prefix == B_prefix and
        they don't satisfy the criteria for operator "greater than or
        equal". If A_prefix != B_prefix, an error MUST be reported. less
        than or equal: A is less than or equal to B if and only if
        A_prefix == B_prefix and they don't satisfy the criteria for
        operator "greater than". If A_prefix != B_prefix, an error MUST
        be reported. subset of: A is a subset of B if and only if every
        IPv6 address in subnet A is present in subnet B. In other words,
        A_prefix &gt;= B_prefix and the high B_prefix bits of A_addr and
        B_addr are equal. superset of: A is a superset of B if and only
        if B is a subset of A.
    :cvar STRING: 'string' is included to allow for regular expressions
        on IOS version strings.
    :cvar VERSION: The version datatype represents a value that is a
        hierarchical list of non-negative integers separated by a single
        character delimiter.  Note that any non-number character can be
        used as a delimiter and that different characters can be used
        within the same version string.  So '#.#-#' is the same as
        '#.#.#' or '#c#c#' where '#' is any non-negative integer.
        Expected operations within OVAL for version values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', and 'less than or equal'. For example '#.#.#' or
        '#-#-#-#' where the numbers to the left are more significant
        than the numbers to the right. When performing an 'equals'
        operation on a version datatype, you should first check the left
        most number for equality. If that fails, then the values are not
        equal. If it succeeds, then check the second left most number
        for equality. Continue checking the numbers from left to right
        until the last number has been checked. If, after testing all
        the previous numbers, the last number is equal then the two
        versions are equal. When performing other operations, such as
        'less than', 'less than or equal', 'greater than, or 'greater
        than or equal', similar logic as above is used. Start with the
        left most number and move from left to right. For each number,
        check if it is less than the number you are testing against. If
        it is, then the version in question is less than the version you
        are testing against. If the number is equal, then move to check
        the next number to the right. For example, to test if 5.7.23 is
        less than or equal to 5.8.0 you first compare 5 to 5. They are
        equal so you move on to compare 7 to 8. 7 is less than 8 so the
        entire test succeeds and 5.7.23 is 'less than or equal' to
        5.8.0. The difference between the 'less than' and 'less than or
        equal' operations is how the last number is handled. If the last
        number is reached, the check should use the given operation
        (either 'less than' and 'less than or equal') to test the
        number. For example, to test if 4.23.6 is greater than 4.23.6
        you first compare 4 to 4. They are equal so you move on to
        compare 23 to 23. They are equal so you move on to compare 6 to
        6. This is the last number in the version and since 6 is not
        greater than 6, the entire test fails and 4.23.6 is not greater
        than 4.23.6. Version strings with a different number of
        components shall be padded with zeros to make them the same
        size. For example, if the version strings '1.2.3' and '6.7.8.9'
        are being compared, then the short one should be padded to
        become '1.2.3.0'.
    """
    BINARY = "binary"
    BOOLEAN = "boolean"
    EVR_STRING = "evr_string"
    DEBIAN_EVR_STRING = "debian_evr_string"
    FILESET_REVISION = "fileset_revision"
    FLOAT_VALUE = "float"
    IOS_VERSION = "ios_version"
    INT_VALUE = "int"
    IPV4_ADDRESS = "ipv4_address"
    IPV6_ADDRESS = "ipv6_address"
    STRING = "string"
    VERSION = "version"


class EntityStateIpaddressStringTypeDatatype(Enum):
    """
    :cvar BINARY: The binary datatype is used to represent hex-encoded
        data that is in raw (non-printable) form. This datatype conforms
        to the W3C Recommendation for binary data meaning that each
        binary octet is encoded as a character tuple, consisting of two
        hexadecimal digits {[0-9a-fA-F]} representing the octet code.
        Expected operations within OVAL for binary values are 'equals'
        and 'not equal'.
    :cvar BOOLEAN: The boolean datatype represents standard boolean
        data, either true or false.  This datatype conforms to the W3C
        Recommendation for boolean data meaning that the following
        literals are legal values: {true, false, 1, 0}.  Expected
        operations within OVAL for boolean values are 'equals' and 'not
        equal'.
    :cvar EVR_STRING: The evr_string datatype represents the epoch,
        version, and release fields as a single version string. It has
        the form "EPOCH:VERSION-RELEASE". Comparisons involving this
        datatype should follow the algorithm of librpm's rpmvercmp()
        function. Expected operations within OVAL for evr_string values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar DEBIAN_EVR_STRING: The debian_evr_string datatype represents
        the epoch, upstream_version, and debian_revision fields, for a
        Debian package, as a single version string. It has the form
        "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Comparisons involving
        this datatype should follow the algorithm outlined in Chapter 5
        of the "Debian Policy Manual"
        (https://www.debian.org/doc/debian-policy/ch-
        controlfields.html#s-f-Version). Note that a null epoch is
        equivalent to a value of '0'. An implementation of this is the
        cmpversions() function in dpkg's enquiry.c. Expected operations
        within OVAL for debian_evr_string values are 'equals', 'not
        equal', 'greater than', 'greater than or equal', 'less than',
        and 'less than or equal'.
    :cvar FILESET_REVISION: The fileset_revision datatype represents the
        version string related to filesets in HP-UX. An example would be
        'A.03.61.00'. For more information, see the HP-UX "Software
        Distributor Administration Guide"
        (http://h20000.www2.hp.com/bc/docs/support/SupportManual/c01919399/c01919399.pdf).
        Expected operations within OVAL for fileset_version values are
        'equals', 'not equal', 'greater than', 'greater than or equal',
        'less than', and 'less than or equal'.
    :cvar FLOAT_VALUE: The float datatype describes standard float data.
        This datatype conforms to the W3C Recommendation for float data
        meaning it is patterned after the IEEE single-precision 32-bit
        floating point type.  The format consists of a decimal followed,
        optionally, by the character 'E' or 'e', followed by an integer
        exponent.  The special values positive and negative infinity and
        not-a-number have are represented by INF, -INF and NaN,
        respectively.  Expected operations within OVAL for float values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar IOS_VERSION: The ios_version datatype describes Cisco IOS
        Train strings. These are in essence version strings for IOS.
        Please refer to Cisco's IOS Reference Guide for information on
        how to compare different Trains as they follow a very specific
        pattern. Expected operations within OVAL for ios_version values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar INT_VALUE: The int datatype describes standard integer data.
        This datatype conforms to the W3C Recommendation for integer
        data which follows the standard mathematical concept of the
        integer numbers.  (no decimal point and infinite range)
        Expected operations within OVAL for int values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', 'less than or equal', 'bitwise and', and 'bitwise or'.
    :cvar IPV4_ADDRESS:
    :cvar IPV6_ADDRESS:
    :cvar STRING:
    :cvar VERSION: The version datatype represents a value that is a
        hierarchical list of non-negative integers separated by a single
        character delimiter.  Note that any non-number character can be
        used as a delimiter and that different characters can be used
        within the same version string.  So '#.#-#' is the same as
        '#.#.#' or '#c#c#' where '#' is any non-negative integer.
        Expected operations within OVAL for version values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', and 'less than or equal'. For example '#.#.#' or
        '#-#-#-#' where the numbers to the left are more significant
        than the numbers to the right. When performing an 'equals'
        operation on a version datatype, you should first check the left
        most number for equality. If that fails, then the values are not
        equal. If it succeeds, then check the second left most number
        for equality. Continue checking the numbers from left to right
        until the last number has been checked. If, after testing all
        the previous numbers, the last number is equal then the two
        versions are equal. When performing other operations, such as
        'less than', 'less than or equal', 'greater than, or 'greater
        than or equal', similar logic as above is used. Start with the
        left most number and move from left to right. For each number,
        check if it is less than the number you are testing against. If
        it is, then the version in question is less than the version you
        are testing against. If the number is equal, then move to check
        the next number to the right. For example, to test if 5.7.23 is
        less than or equal to 5.8.0 you first compare 5 to 5. They are
        equal so you move on to compare 7 to 8. 7 is less than 8 so the
        entire test succeeds and 5.7.23 is 'less than or equal' to
        5.8.0. The difference between the 'less than' and 'less than or
        equal' operations is how the last number is handled. If the last
        number is reached, the check should use the given operation
        (either 'less than' and 'less than or equal') to test the
        number. For example, to test if 4.23.6 is greater than 4.23.6
        you first compare 4 to 4. They are equal so you move on to
        compare 23 to 23. They are equal so you move on to compare 6 to
        6. This is the last number in the version and since 6 is not
        greater than 6, the entire test fails and 4.23.6 is not greater
        than 4.23.6. Version strings with a different number of
        components shall be padded with zeros to make them the same
        size. For example, if the version strings '1.2.3' and '6.7.8.9'
        are being compared, then the short one should be padded to
        become '1.2.3.0'.
    """
    BINARY = "binary"
    BOOLEAN = "boolean"
    EVR_STRING = "evr_string"
    DEBIAN_EVR_STRING = "debian_evr_string"
    FILESET_REVISION = "fileset_revision"
    FLOAT_VALUE = "float"
    IOS_VERSION = "ios_version"
    INT_VALUE = "int"
    IPV4_ADDRESS = "ipv4_address"
    IPV6_ADDRESS = "ipv6_address"
    STRING = "string"
    VERSION = "version"


class FilterActionEnumeration(Enum):
    """
    The FilterActionEnumeration simple type defines the different options for
    filtering sets of items.

    :cvar EXCLUDE: The exclude value specifies that all items that match
        the filter shall be excluded from set that the filter is applied
        to.
    :cvar INCLUDE: The include value specifies that only items that
        match the filter shall be included in the set that the filter is
        applied to.
    """
    EXCLUDE = "exclude"
    INCLUDE = "include"


class SetOperatorEnumeration(Enum):
    """The SetOperatorEnumeration simple type defines acceptable set
    operations.

    Set operations are used to take multiple different sets of objects
    within OVAL and merge them into a single unique set. The different
    operators that guide this merge are defined below. For each
    operator, if only a single object has been supplied, then the
    resulting set is simply that complete object.

    :cvar COMPLEMENT: The complement operator is defined in OVAL as a
        relative complement. The resulting unique set contains
        everything that belongs to the first declared set that is not
        part of the second declared set. If A and B are sets (with A
        being the first declared set), then the relative complement is
        the set of elements in A, but not in B, with the duplicates
        removed.
    :cvar INTERSECTION: The intersection of two sets in OVAL results in
        a unique set that contains everything that belongs to both sets
        in the collection, but nothing else. If A and B are sets, then
        the intersection of A and B contains all the elements of A that
        also belong to B, but no other elements, with the duplicates
        removed.
    :cvar UNION: The union of two sets in OVAL results in a unique set
        that contains everything that belongs to either of the original
        sets. If A and B are sets, then the union of A and B contains
        all the elements of A and all elements of B, with the duplicates
        removed.
    """
    COMPLEMENT = "COMPLEMENT"
    INTERSECTION = "INTERSECTION"
    UNION = "UNION"
