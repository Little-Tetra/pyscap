from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Function:
    """Function of the Person defined.

    Example: Managing Director, CEO, Marketing Manager, etc.

    :ivar content:
    :ivar code: Indicates the name element code defined by postal
        standard groups like ECCMA, ADIS, UN/PROLIST for postal
        services.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class NameLineType:
    """
    :ivar content:
    :ivar type: Type of data defined as a free format text. Example:
        Former name, Nick name, Known as, etc. or anything else to help
        identify the line as part of the name.
    :ivar name_type: Clarifies the meaning of the element. Example:
        First Name can be Christian name, Given name, first name, etc.
    :ivar code: Indicates the name element code defined by postal
        standard groups like ECCMA, ADIS, UN/PROLIST for postal
        services.
    :ivar other_attributes:
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    name_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameType",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class OrganisationNameDetails:
    """
    A container for organisation name details.

    :ivar name_line: Free format text that defines the organisation name
        or parts of it.
    :ivar organisation_name: Name of the organisation. Example: MSI
        Business Solutions in "MSI Business Solutions Pty. Ltd" or the
        whole name itself
    :ivar organisation_type: Indicates the legal status of an
        organisation. Example: Pty, Ltd, GmbH, etc. Pty. Ltd. in "XYZ
        Pty. Ltd"
    :ivar type: Type of Organisation Name. Example: Former name, Known
        as, etc
    :ivar name_details_key_ref: Reference to another NameDetails element
        with no foreign key reinforcement. The referenced element may be
        out of the document and the document is still valid.
    :ivar other_attributes:
    :ivar organisation_former_name: Name history for the organisation
    :ivar organisation_known_as: Any other names the organisation can be
        known under.
    :ivar other_element: Use this to import/use/reference name elements
        from other namespaces
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0"

    name_line: List[NameLineType] = field(
        default_factory=list,
        metadata={
            "name": "NameLine",
            "type": "Element",
        }
    )
    organisation_name: List["OrganisationNameDetails.OrganisationName"] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationName",
            "type": "Element",
        }
    )
    organisation_type: List["OrganisationNameDetails.OrganisationType"] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationType",
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    name_details_key_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameDetailsKeyRef",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    organisation_former_name: List["OrganisationNameDetails.OrganisationFormerName"] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationFormerName",
            "type": "Element",
        }
    )
    organisation_known_as: List["OrganisationNameDetails.OrganisationKnownAs"] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationKnownAs",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )

    @dataclass
    class OrganisationFormerName:
        """
        :ivar name_line: Free format text that defines the organisation
            name or parts of it.
        :ivar organisation_name: Name of the organisation. Example: MSI
            Business Solutions in "MSI Business Solutions Pty. Ltd" or
            the whole name itself
        :ivar organisation_type: Indicates the legal status of an
            organisation. Example: Pty, Ltd, GmbH, etc. Pty. Ltd. in
            "XYZ Pty. Ltd"
        :ivar type: Type of Organisation Name. Example: Former name,
            Known as, etc
        :ivar name_details_key_ref: Reference to another NameDetails
            element with no foreign key reinforcement. The referenced
            element may be out of the document and the document is still
            valid.
        :ivar other_attributes:
        :ivar other_element: Use this to import/use/reference name
            elements from other namespaces
        :ivar valid_from: The first date when the name is valid.
            Inclusive.
        :ivar valid_to: The last date when the name is valid. Inclusive.
        """
        name_line: List[NameLineType] = field(
            default_factory=list,
            metadata={
                "name": "NameLine",
                "type": "Element",
            }
        )
        organisation_name: List["OrganisationNameDetails.OrganisationFormerName.OrganisationName"] = field(
            default_factory=list,
            metadata={
                "name": "OrganisationName",
                "type": "Element",
            }
        )
        organisation_type: List["OrganisationNameDetails.OrganisationFormerName.OrganisationType"] = field(
            default_factory=list,
            metadata={
                "name": "OrganisationType",
                "type": "Element",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_details_key_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameDetailsKeyRef",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        valid_from: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValidFrom",
                "type": "Attribute",
            }
        )
        valid_to: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValidTo",
                "type": "Attribute",
            }
        )

        @dataclass
        class OrganisationName:
            """
            :ivar content:
            :ivar type: Type of Organisation name. Example: Official,
                Legal, Un-official, etc
            :ivar name_type: Defines the name type of the Organisation
                name. Example: Former name, new name, abbreviated name
                etc.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class OrganisationType:
            """
            :ivar content:
            :ivar type: Defines the Type of Organisation Type. Example:
                Abbreviation, Legal Type, etc.
            :ivar name_type: Defines the name type of Organisation Type.
                Example: Private, Public, proprietary, etc.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

    @dataclass
    class OrganisationKnownAs:
        """
        :ivar name_line: Free format text that defines the organisation
            name or parts of it.
        :ivar organisation_name: Name of the organisation. Example: MSI
            Business Solutions in "MSI Business Solutions Pty. Ltd" or
            the whole name itself
        :ivar organisation_type: Indicates the legal status of an
            organisation. Example: Pty, Ltd, GmbH, etc. Pty. Ltd. in
            "XYZ Pty. Ltd"
        :ivar type: Type of Organisation Name. Example: Former name,
            Known as, etc
        :ivar name_details_key_ref: Reference to another NameDetails
            element with no foreign key reinforcement. The referenced
            element may be out of the document and the document is still
            valid.
        :ivar other_attributes:
        :ivar other_element: Use this to import/use/reference name
            elements from other namespaces
        :ivar valid_from: The first date when the name is valid.
            Inclusive.
        :ivar valid_to: The last date when the name is valid. Inclusive.
        """
        name_line: List[NameLineType] = field(
            default_factory=list,
            metadata={
                "name": "NameLine",
                "type": "Element",
            }
        )
        organisation_name: List["OrganisationNameDetails.OrganisationKnownAs.OrganisationName"] = field(
            default_factory=list,
            metadata={
                "name": "OrganisationName",
                "type": "Element",
            }
        )
        organisation_type: List["OrganisationNameDetails.OrganisationKnownAs.OrganisationType"] = field(
            default_factory=list,
            metadata={
                "name": "OrganisationType",
                "type": "Element",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_details_key_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameDetailsKeyRef",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        valid_from: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValidFrom",
                "type": "Attribute",
            }
        )
        valid_to: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValidTo",
                "type": "Attribute",
            }
        )

        @dataclass
        class OrganisationName:
            """
            :ivar content:
            :ivar type: Type of Organisation name. Example: Official,
                Legal, Un-official, etc
            :ivar name_type: Defines the name type of the Organisation
                name. Example: Former name, new name, abbreviated name
                etc.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class OrganisationType:
            """
            :ivar content:
            :ivar type: Defines the Type of Organisation Type. Example:
                Abbreviation, Legal Type, etc.
            :ivar name_type: Defines the name type of Organisation Type.
                Example: Private, Public, proprietary, etc.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

    @dataclass
    class OrganisationName:
        """
        :ivar content:
        :ivar type: Type of Organisation name. Example: Official, Legal,
            Un-official, etc
        :ivar name_type: Defines the name type of the Organisation name.
            Example: Former name, new name, abbreviated name etc.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class OrganisationType:
        """
        :ivar content:
        :ivar type: Defines the Type of Organisation Type. Example:
            Abbreviation, Legal Type, etc.
        :ivar name_type: Defines the name type of Organisation Type.
            Example: Private, Public, proprietary, etc.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class PersonName:
    """
    Container for person name details.

    :ivar name_line: Name or part of a name defined as a free format
        text.
    :ivar preceding_title: His Excellency,Estate of the Late ...
    :ivar title: Greeting title. Example: Mr, Dr, Ms, Herr, etc. Can
        have multiple titles.
    :ivar first_name: Represents the position of the name in a name
        string. Can be Given Name, Christian Name, Surname, family name,
        etc. Use the attribute "NameType" to define what type this name
        is.
    :ivar middle_name: Middle name (essential part of the name for many
        nationalities). Represents the position of the name in the name
        string. Example: Sakthi in "Nivetha Sakthi Shantha". Can have
        multiple middle names.
    :ivar name_prefix: de, van, van de, von, etc. Example: Derick de
        Clarke
    :ivar last_name: Represents the position of the name in a name
        string. Can be Given Name, Christian Name, Surname, family name,
        etc. Use the attribute "NameType" to define what type this name
        is.
    :ivar other_name: All other names, e.g.: Yousuf Khan al Hatab al
        Sayad
    :ivar alias: Nick Name, Pet name, etc..
    :ivar generation_identifier: Jnr, Thr Third, III
    :ivar suffix: Could be compressed initials - PhD, VC, QC
    :ivar general_suffix: Deceased, Retired ...
    :ivar type: Type of Name of a person. Example: Full name, Former
        Name, Known As, etc.
    :ivar code: Indicates the name element code defined by postal
        standard groups like ECCMA, ADIS, UN/PROLIST for postal
        services.
    :ivar name_details_key_ref: Reference to another NameDetails element
        with no foreign key reinforcement. The referenced element may be
        out of the document and the document is still valid.
    :ivar other_attributes:
    :ivar former_name: Example: maiden name
    :ivar known_as: Sometimes the same person is known under different
        unofficial or official names
    :ivar other_element: Use this to import/use/reference name elements
        from other namespaces
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0"

    name_line: List[NameLineType] = field(
        default_factory=list,
        metadata={
            "name": "NameLine",
            "type": "Element",
        }
    )
    preceding_title: List["PersonName.PrecedingTitle"] = field(
        default_factory=list,
        metadata={
            "name": "PrecedingTitle",
            "type": "Element",
        }
    )
    title: List["PersonName.Title"] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
        }
    )
    first_name: List["PersonName.FirstName"] = field(
        default_factory=list,
        metadata={
            "name": "FirstName",
            "type": "Element",
        }
    )
    middle_name: List["PersonName.MiddleName"] = field(
        default_factory=list,
        metadata={
            "name": "MiddleName",
            "type": "Element",
        }
    )
    name_prefix: Optional["PersonName.NamePrefix"] = field(
        default=None,
        metadata={
            "name": "NamePrefix",
            "type": "Element",
        }
    )
    last_name: List["PersonName.LastName"] = field(
        default_factory=list,
        metadata={
            "name": "LastName",
            "type": "Element",
        }
    )
    other_name: List["PersonName.OtherName"] = field(
        default_factory=list,
        metadata={
            "name": "OtherName",
            "type": "Element",
        }
    )
    alias: List["PersonName.Alias"] = field(
        default_factory=list,
        metadata={
            "name": "Alias",
            "type": "Element",
        }
    )
    generation_identifier: List["PersonName.GenerationIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "GenerationIdentifier",
            "type": "Element",
        }
    )
    suffix: List["PersonName.Suffix"] = field(
        default_factory=list,
        metadata={
            "name": "Suffix",
            "type": "Element",
        }
    )
    general_suffix: Optional["PersonName.GeneralSuffix"] = field(
        default=None,
        metadata={
            "name": "GeneralSuffix",
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    name_details_key_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameDetailsKeyRef",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    former_name: List["PersonName.FormerName"] = field(
        default_factory=list,
        metadata={
            "name": "FormerName",
            "type": "Element",
        }
    )
    known_as: List["PersonName.KnownAs"] = field(
        default_factory=list,
        metadata={
            "name": "KnownAs",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )

    @dataclass
    class FormerName:
        """
        :ivar name_line: Name or part of a name defined as a free format
            text.
        :ivar preceding_title: His Excellency,Estate of the Late ...
        :ivar title: Greeting title. Example: Mr, Dr, Ms, Herr, etc. Can
            have multiple titles.
        :ivar first_name: Represents the position of the name in a name
            string. Can be Given Name, Christian Name, Surname, family
            name, etc. Use the attribute "NameType" to define what type
            this name is.
        :ivar middle_name: Middle name (essential part of the name for
            many nationalities). Represents the position of the name in
            the name string. Example: Sakthi in "Nivetha Sakthi
            Shantha". Can have multiple middle names.
        :ivar name_prefix: de, van, van de, von, etc. Example: Derick de
            Clarke
        :ivar last_name: Represents the position of the name in a name
            string. Can be Given Name, Christian Name, Surname, family
            name, etc. Use the attribute "NameType" to define what type
            this name is.
        :ivar other_name: All other names, e.g.: Yousuf Khan al Hatab al
            Sayad
        :ivar alias: Nick Name, Pet name, etc..
        :ivar generation_identifier: Jnr, Thr Third, III
        :ivar suffix: Could be compressed initials - PhD, VC, QC
        :ivar general_suffix: Deceased, Retired ...
        :ivar type: Type of Name of a person. Example: Full name, Former
            Name, Known As, etc.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar name_details_key_ref: Reference to another NameDetails
            element with no foreign key reinforcement. The referenced
            element may be out of the document and the document is still
            valid.
        :ivar other_attributes:
        :ivar other_element:
        :ivar valid_from: The first date when the name is valid.
            Inclusive.
        :ivar valid_to: The last date when the name is valid. Inclusive.
        """
        name_line: List[NameLineType] = field(
            default_factory=list,
            metadata={
                "name": "NameLine",
                "type": "Element",
            }
        )
        preceding_title: List["PersonName.FormerName.PrecedingTitle"] = field(
            default_factory=list,
            metadata={
                "name": "PrecedingTitle",
                "type": "Element",
            }
        )
        title: List["PersonName.FormerName.Title"] = field(
            default_factory=list,
            metadata={
                "name": "Title",
                "type": "Element",
            }
        )
        first_name: List["PersonName.FormerName.FirstName"] = field(
            default_factory=list,
            metadata={
                "name": "FirstName",
                "type": "Element",
            }
        )
        middle_name: List["PersonName.FormerName.MiddleName"] = field(
            default_factory=list,
            metadata={
                "name": "MiddleName",
                "type": "Element",
            }
        )
        name_prefix: Optional["PersonName.FormerName.NamePrefix"] = field(
            default=None,
            metadata={
                "name": "NamePrefix",
                "type": "Element",
            }
        )
        last_name: List["PersonName.FormerName.LastName"] = field(
            default_factory=list,
            metadata={
                "name": "LastName",
                "type": "Element",
            }
        )
        other_name: List["PersonName.FormerName.OtherName"] = field(
            default_factory=list,
            metadata={
                "name": "OtherName",
                "type": "Element",
            }
        )
        alias: List["PersonName.FormerName.Alias"] = field(
            default_factory=list,
            metadata={
                "name": "Alias",
                "type": "Element",
            }
        )
        generation_identifier: List["PersonName.FormerName.GenerationIdentifier"] = field(
            default_factory=list,
            metadata={
                "name": "GenerationIdentifier",
                "type": "Element",
            }
        )
        suffix: List["PersonName.FormerName.Suffix"] = field(
            default_factory=list,
            metadata={
                "name": "Suffix",
                "type": "Element",
            }
        )
        general_suffix: Optional["PersonName.FormerName.GeneralSuffix"] = field(
            default=None,
            metadata={
                "name": "GeneralSuffix",
                "type": "Element",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        name_details_key_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameDetailsKeyRef",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        valid_from: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValidFrom",
                "type": "Attribute",
            }
        )
        valid_to: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValidTo",
                "type": "Attribute",
            }
        )

        @dataclass
        class PrecedingTitle:
            """
            :ivar content:
            :ivar type: Type of Preceding Title. Example:  Honorary
                title.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class Title:
            """
            :ivar content:
            :ivar type: Type of Title. Example: Plural Titles such as
                MESSRS, Formal Degree, Honarary Degree, Sex (Mr, Mrs)
                etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class FirstName:
            """
            :ivar content:
            :ivar type: Type of first name. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the name type of first name.
                Example: Given Name, Christian Name, Father's Name, etc.
                In some countries, First name could be a Family Name or
                a SurName. Use this attribute to define the type for
                this name.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class MiddleName:
            """
            :ivar content:
            :ivar type: Type of middle name. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the name type of Middle Name.
                Example: First name, middle name, maiden name, father's
                name, given name, etc.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class NamePrefix:
            """
            :ivar content:
            :ivar type: Type of last name prefix. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the type of name associated with
                the NamePrefix. For example the type of name is LastName
                and this prefix is the prefix for this last name.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class LastName:
            """
            :ivar content:
            :ivar type: Type of last name. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the name type of Last Name.
                Example: Father's name, Family name, Sur Name, Mother's
                Name, etc. In some countries, Last name could be the
                given name or first name.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class OtherName:
            """
            :ivar content:
            :ivar type: Type of Other name. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the name type of Other Name.
                Example: Maiden Name, Patronymic name, Matronymic name,
                etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class Alias:
            """
            :ivar content:
            :ivar type: Type of Alias. Example: Official, UnOfficial,
                Close Circle, etc
            :ivar name_type: Defines the name type of Alias. Example:
                Nick Name, Pet Name, etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class GenerationIdentifier:
            """
            :ivar content:
            :ivar type: Defines the type of generation identifier.
                Example: Family Titles
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class Suffix:
            """
            :ivar content:
            :ivar type: Defines the type of Suffix. Example: Compressed
                Initials, Full suffixes, etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class GeneralSuffix:
            """
            :ivar content:
            :ivar type: Defines the type of General Suffix. Example:
                Employment Status, Living Status, etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

    @dataclass
    class KnownAs:
        """
        :ivar name_line: Name or part of a name defined as a free format
            text.
        :ivar preceding_title: His Excellency,Estate of the Late ...
        :ivar title: Greeting title. Example: Mr, Dr, Ms, Herr, etc. Can
            have multiple titles.
        :ivar first_name: Represents the position of the name in a name
            string. Can be Given Name, Christian Name, Surname, family
            name, etc. Use the attribute "NameType" to define what type
            this name is.
        :ivar middle_name: Middle name (essential part of the name for
            many nationalities). Represents the position of the name in
            the name string. Example: Sakthi in "Nivetha Sakthi
            Shantha". Can have multiple middle names.
        :ivar name_prefix: de, van, van de, von, etc. Example: Derick de
            Clarke
        :ivar last_name: Represents the position of the name in a name
            string. Can be Given Name, Christian Name, Surname, family
            name, etc. Use the attribute "NameType" to define what type
            this name is.
        :ivar other_name: All other names, e.g.: Yousuf Khan al Hatab al
            Sayad
        :ivar alias: Nick Name, Pet name, etc..
        :ivar generation_identifier: Jnr, Thr Third, III
        :ivar suffix: Could be compressed initials - PhD, VC, QC
        :ivar general_suffix: Deceased, Retired ...
        :ivar type: Type of Name of a person. Example: Full name, Former
            Name, Known As, etc.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar name_details_key_ref: Reference to another NameDetails
            element with no foreign key reinforcement. The referenced
            element may be out of the document and the document is still
            valid.
        :ivar other_attributes:
        :ivar other_element:
        :ivar valid_from: The first date when the name is valid.
            Inclusive.
        :ivar valid_to: The last date when the name is valid. Inclusive.
        """
        name_line: List[NameLineType] = field(
            default_factory=list,
            metadata={
                "name": "NameLine",
                "type": "Element",
            }
        )
        preceding_title: List["PersonName.KnownAs.PrecedingTitle"] = field(
            default_factory=list,
            metadata={
                "name": "PrecedingTitle",
                "type": "Element",
            }
        )
        title: List["PersonName.KnownAs.Title"] = field(
            default_factory=list,
            metadata={
                "name": "Title",
                "type": "Element",
            }
        )
        first_name: List["PersonName.KnownAs.FirstName"] = field(
            default_factory=list,
            metadata={
                "name": "FirstName",
                "type": "Element",
            }
        )
        middle_name: List["PersonName.KnownAs.MiddleName"] = field(
            default_factory=list,
            metadata={
                "name": "MiddleName",
                "type": "Element",
            }
        )
        name_prefix: Optional["PersonName.KnownAs.NamePrefix"] = field(
            default=None,
            metadata={
                "name": "NamePrefix",
                "type": "Element",
            }
        )
        last_name: List["PersonName.KnownAs.LastName"] = field(
            default_factory=list,
            metadata={
                "name": "LastName",
                "type": "Element",
            }
        )
        other_name: List["PersonName.KnownAs.OtherName"] = field(
            default_factory=list,
            metadata={
                "name": "OtherName",
                "type": "Element",
            }
        )
        alias: List["PersonName.KnownAs.Alias"] = field(
            default_factory=list,
            metadata={
                "name": "Alias",
                "type": "Element",
            }
        )
        generation_identifier: List["PersonName.KnownAs.GenerationIdentifier"] = field(
            default_factory=list,
            metadata={
                "name": "GenerationIdentifier",
                "type": "Element",
            }
        )
        suffix: List["PersonName.KnownAs.Suffix"] = field(
            default_factory=list,
            metadata={
                "name": "Suffix",
                "type": "Element",
            }
        )
        general_suffix: Optional["PersonName.KnownAs.GeneralSuffix"] = field(
            default=None,
            metadata={
                "name": "GeneralSuffix",
                "type": "Element",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        name_details_key_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameDetailsKeyRef",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        valid_from: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValidFrom",
                "type": "Attribute",
            }
        )
        valid_to: Optional[str] = field(
            default=None,
            metadata={
                "name": "ValidTo",
                "type": "Attribute",
            }
        )

        @dataclass
        class PrecedingTitle:
            """
            :ivar content:
            :ivar type: Type of Preceding Title. Example:  Honorary
                title.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class Title:
            """
            :ivar content:
            :ivar type: Type of Title. Example: Plural Titles such as
                MESSRS, Formal Degree, Honarary Degree, Sex (Mr, Mrs)
                etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class FirstName:
            """
            :ivar content:
            :ivar type: Type of first name. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the name type of first name.
                Example: Given Name, Christian Name, Father's Name, etc.
                In some countries, First name could be a Family Name or
                a SurName. Use this attribute to define the type for
                this name.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class MiddleName:
            """
            :ivar content:
            :ivar type: Type of middle name. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the name type of Middle Name.
                Example: First name, middle name, maiden name, father's
                name, given name, etc.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class NamePrefix:
            """
            :ivar content:
            :ivar type: Type of last name prefix. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the type of name associated with
                the NamePrefix. For example the type of name is LastName
                and this prefix is the prefix for this last name.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class LastName:
            """
            :ivar content:
            :ivar type: Type of last name. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the name type of Last Name.
                Example: Father's name, Family name, Sur Name, Mother's
                Name, etc. In some countries, Last name could be the
                given name or first name.
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class OtherName:
            """
            :ivar content:
            :ivar type: Type of Other name. Example: Official, Un-
                official, abbreviation, initial, etc
            :ivar name_type: Defines the name type of Other Name.
                Example: Maiden Name, Patronymic name, Matronymic name,
                etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class Alias:
            """
            :ivar content:
            :ivar type: Type of Alias. Example: Official, UnOfficial,
                Close Circle, etc
            :ivar name_type: Defines the name type of Alias. Example:
                Nick Name, Pet Name, etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            name_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NameType",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class GenerationIdentifier:
            """
            :ivar content:
            :ivar type: Defines the type of generation identifier.
                Example: Family Titles
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class Suffix:
            """
            :ivar content:
            :ivar type: Defines the type of Suffix. Example: Compressed
                Initials, Full suffixes, etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class GeneralSuffix:
            """
            :ivar content:
            :ivar type: Defines the type of General Suffix. Example:
                Employment Status, Living Status, etc
            :ivar code: Indicates the name element code defined by
                postal standard groups like ECCMA, ADIS, UN/PROLIST for
                postal services.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

    @dataclass
    class PrecedingTitle:
        """
        :ivar content:
        :ivar type: Type of Preceding Title. Example:  Honorary title.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class Title:
        """
        :ivar content:
        :ivar type: Type of Title. Example: Plural Titles such as
            MESSRS, Formal Degree, Honarary Degree, Sex (Mr, Mrs) etc
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class FirstName:
        """
        :ivar content:
        :ivar type: Type of first name. Example: Official, Un-official,
            abbreviation, initial, etc
        :ivar name_type: Defines the name type of first name. Example:
            Given Name, Christian Name, Father's Name, etc. In some
            countries, First name could be a Family Name or a SurName.
            Use this attribute to define the type for this name.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class MiddleName:
        """
        :ivar content:
        :ivar type: Type of middle name. Example: Official, Un-official,
            abbreviation, initial, etc
        :ivar name_type: Defines the name type of Middle Name. Example:
            First name, middle name, maiden name, father's name, given
            name, etc.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class NamePrefix:
        """
        :ivar content:
        :ivar type: Type of last name prefix. Example: Official, Un-
            official, abbreviation, initial, etc
        :ivar name_type: Defines the type of name associated with the
            NamePrefix. For example the type of name is LastName and
            this prefix is the prefix for this last name.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class LastName:
        """
        :ivar content:
        :ivar type: Type of last name. Example: Official, Un-official,
            abbreviation, initial, etc
        :ivar name_type: Defines the name type of Last Name. Example:
            Father's name, Family name, Sur Name, Mother's Name, etc. In
            some countries, Last name could be the given name or first
            name.
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class OtherName:
        """
        :ivar content:
        :ivar type: Type of Other name. Example: Official, Un-official,
            abbreviation, initial, etc
        :ivar name_type: Defines the name type of Other Name. Example:
            Maiden Name, Patronymic name, Matronymic name, etc
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class Alias:
        """
        :ivar content:
        :ivar type: Type of Alias. Example: Official, UnOfficial, Close
            Circle, etc
        :ivar name_type: Defines the name type of Alias. Example: Nick
            Name, Pet Name, etc
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        name_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class GenerationIdentifier:
        """
        :ivar content:
        :ivar type: Defines the type of generation identifier. Example:
            Family Titles
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class Suffix:
        """
        :ivar content:
        :ivar type: Defines the type of Suffix. Example: Compressed
            Initials, Full suffixes, etc
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class GeneralSuffix:
        """
        :ivar content:
        :ivar type: Defines the type of General Suffix. Example:
            Employment Status, Living Status, etc
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class JointPersonName:
    """A container to define more than one person name.

    Example: Mrs Mary Johnson and Mr.Patrick Johnson

    :ivar name_line: Name or part of the name as a free format text. If
        the name structure has to be broken down into individual
        elements, use PersonName Container.
    :ivar person_name: Use this element to specify every member
        separately.
    :ivar other_element: Use this to import/use/reference name elements
        from other namespaces
    :ivar joint_name_connector: The connector used to join more than one
        person name. Example: Mr Hunt AND Mrs Clark, where AND is the
        JointNameConnector
    :ivar code: Indicates the name element code defined by postal
        standard groups like ECCMA, ADIS, UN/PROLIST for postal
        services.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0"

    name_line: List[NameLineType] = field(
        default_factory=list,
        metadata={
            "name": "NameLine",
            "type": "Element",
            "sequential": True,
        }
    )
    person_name: List[PersonName] = field(
        default_factory=list,
        metadata={
            "name": "PersonName",
            "type": "Element",
            "sequential": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    joint_name_connector: Optional[str] = field(
        default=None,
        metadata={
            "name": "JointNameConnector",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class NameDetails:
    """
    Container for defining the name of a Person or an Organisation.

    :ivar name_line: Define name as a free format text. Use this when
        the type of the entity (person or organisation) is unknown, or
        not broken into individual elements or is beyond the provided
        types.
    :ivar person_name:
    :ivar joint_person_name:
    :ivar organisation_name_details:
    :ivar party_type: Indicates the type of entity i.e described namely,
        Person or an Organisation. An Organisation could be: Club,
        Association, Company, etc
    :ivar code: Indicates the name element code defined by postal
        standard groups like ECCMA, ADIS, UN/PROLIST for postal
        services.
    :ivar other_attributes:
    :ivar addressee_indicator: Specific for name and address where the
        addressee is specified. eg. ATTENTION, ter attentie van (in
        Holland), etc
    :ivar function:
    :ivar dependency_name: Container for a name of a dependent person or
        organisation. Example: Ram Kumar, C/O MSI Business Solutions
        DependencyType: Person-Person/Person-Organisation Relationship
        (care of, wife of, position, etc). Can have sublement with name
        structure or reference another top-level element.
    :ivar other_element: Use this to import/use/reference name elements
        from other namespaces
    :ivar name_details_key: Key identifier for the element for not
        reinforced references from other elements. Not required to be
        unique for the document to be valid, but application may get
        confused if not unique. Extend this schema adding unique
        contraint if needed.
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0"

    name_line: List[NameLineType] = field(
        default_factory=list,
        metadata={
            "name": "NameLine",
            "type": "Element",
        }
    )
    person_name: Optional[PersonName] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
        }
    )
    joint_person_name: Optional[JointPersonName] = field(
        default=None,
        metadata={
            "name": "JointPersonName",
            "type": "Element",
        }
    )
    organisation_name_details: Optional[OrganisationNameDetails] = field(
        default=None,
        metadata={
            "name": "OrganisationNameDetails",
            "type": "Element",
        }
    )
    party_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartyType",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    addressee_indicator: Optional["NameDetails.AddresseeIndicator"] = field(
        default=None,
        metadata={
            "name": "AddresseeIndicator",
            "type": "Element",
        }
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
        }
    )
    dependency_name: Optional["NameDetails.DependencyName"] = field(
        default=None,
        metadata={
            "name": "DependencyName",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    name_details_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameDetailsKey",
            "type": "Attribute",
        }
    )

    @dataclass
    class AddresseeIndicator:
        """
        :ivar content:
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class DependencyName:
        """
        :ivar name_line: Define name as a free format text. Use this
            when the type of the entity (person or organisation) is
            unknown, or not broken into individual elements or is beyond
            the provided types.
        :ivar person_name:
        :ivar joint_person_name:
        :ivar organisation_name_details:
        :ivar party_type: Indicates the type of entity i.e described
            namely, Person or an Organisation. An Organisation could be:
            Club, Association, Company, etc
        :ivar code: Indicates the name element code defined by postal
            standard groups like ECCMA, ADIS, UN/PROLIST for postal
            services.
        :ivar other_attributes:
        :ivar other_element: Use this to import/use/reference elements
            from other namespaces
        :ivar dependency_type: Description of the dependency: in trust
            of, on behalf of, etc.
        :ivar name_details_key_ref: Reference to another NameDetails
            element with no foreign key reinforcement. The referenced
            element may be out of the document and the document is still
            valid.
        """
        name_line: List[NameLineType] = field(
            default_factory=list,
            metadata={
                "name": "NameLine",
                "type": "Element",
            }
        )
        person_name: Optional[PersonName] = field(
            default=None,
            metadata={
                "name": "PersonName",
                "type": "Element",
            }
        )
        joint_person_name: Optional[JointPersonName] = field(
            default=None,
            metadata={
                "name": "JointPersonName",
                "type": "Element",
            }
        )
        organisation_name_details: Optional[OrganisationNameDetails] = field(
            default=None,
            metadata={
                "name": "OrganisationNameDetails",
                "type": "Element",
            }
        )
        party_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "PartyType",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        dependency_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "DependencyType",
                "type": "Attribute",
            }
        )
        name_details_key_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameDetailsKeyRef",
                "type": "Attribute",
            }
        )


@dataclass
class XNl:
    """
    Root element to define name of a Person or an Organisation  in detail.

    :ivar name_details:
    :ivar other_element: Use this to import/use/reference name elements
        from other namespaces
    :ivar version: DTD version. This attribute is not used for schema
        and exists only for DTD compatibility.
    :ivar other_attributes:
    """

    class Meta:
        name = "xNL"
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0"

    name_details: List[NameDetails] = field(
        default_factory=list,
        metadata={
            "name": "NameDetails",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
