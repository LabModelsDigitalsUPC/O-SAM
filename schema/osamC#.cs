public class o_sam
    {

        public class StructuralAnalysisModel
        {
            public string id;
            public string name;
            public Units units;
            public List<StructuralObject> objects;
            public Assembly assembly;
            public List<Material> materials;
            public List<Section> sections;
            public List<BoundaryCondition> bc;
            public List<LoadCase> loadCases;
            public List<Load> loads;

            public StructuralAnalysisModel(string id, string name, Units units, List<StructuralObject> objects, Assembly assembly, List<Material> materials, List<Section> sections,
                List<BoundaryCondition> bc, List<LoadCase> loadCases, List<Load> loads)
            {
                this.id = id;
                this.name = name;
                this.units = units;
                this.objects = objects;
                this.assembly = assembly;
                this.materials = materials;
                this.sections = sections;
                this.bc = bc;
                this.loadCases = loadCases;
                this.loads = loads;
            }
        }

        public class Units
        {
            public string force;
            public string length;
            public string temperature;
            public string time;
            public string mass;

            public Units(string force, string length, string temperature, string time, string mass)
            {
                this.force = force;
                this.length = length;
                this.temperature = temperature;
                this.time = time;
                this.mass = mass;
            }
        }

        public class StructuralObject
        {
            public string id;
            public string name;
            public Mesh mesh;
            public CoordinateSystem coordinateSystem;

            public StructuralObject(string id, string name, Mesh mesh, CoordinateSystem coordinateSystem)
            {
                this.id = id;
                this.name = name;
                this.mesh = mesh;
                this.coordinateSystem = coordinateSystem;
            }
        }

        public class CoordinateSystem
        {
            public Vector3D xAxis;
            public Vector3D yAxis;
            public Vector3D zAxis;

            public CoordinateSystem(Vector3D xAxis, Vector3D yAxis, Vector3D zAxis)
            {
                this.xAxis = xAxis;
                this.yAxis = yAxis;
                this.zAxis = zAxis;
            }
        }

        public class Vector3D
        {
            public double X;
            public double Y;
            public double Z;

            public Vector3D(double X, double Y, double Z)
            {
                this.X = X;
                this.Y = Y;
                this.Z = Z;
            }
        }


        public class Mesh
        {
            public int node_count;
            public int el_count;
            public List<Node> nodes;
            public List<Element> elements;

            public Mesh(int node_count, int el_count, List<Node> nodes, List<Element> elements)
            {
                this.node_count = node_count;
                this.el_count = el_count;
                this.nodes = nodes;
                this.elements = elements;
            }
        }

        public class Assembly
        {
            public string name;
            public List<Instance> instances;

            public Assembly(string name, List<Instance> instances)
            {
                this.name = name;
                this.instances = instances;
            }
        }

        public class Instance
        {
            public string id;
            public string name;
            public string referenced_object;
            public List<Nsets> nsets;
            public List<Elsets> elsets;
            public Vector3D translation;
            public RotationSpec rotation;

            public Instance(string id, string name, string referenced_object, List<Nsets> nsets, List<Elsets> elsets,
                Vector3D translation, RotationSpec rotation)
            {
                this.id = id;
                this.name = name;
                this.referenced_object = referenced_object;
                this.nsets = nsets;
                this.elsets = elsets;
                this.translation = translation;
                this.rotation = rotation;
            }
        }

        // Point A, point B (defining the rotation axis) and the rotation angle - the
        // shape osam_to_inp.py's _write_instance expects for Instance.rotation when
        // populated (osam.py itself leaves rotation/translation as Optional[Any]).
        public class RotationSpec
        {
            public Vector3D A;
            public Vector3D B;
            public double angle;

            public RotationSpec(Vector3D A, Vector3D B, double angle)
            {
                this.A = A;
                this.B = B;
                this.angle = angle;
            }
        }

        public class Material
        {
            public string name;
            public string category;
            public string type;
            public double mass_density;
            public Elastic elastic;
            public Plastic plastic;

            public Material(string name, string category, string type, double mass_density, Elastic elastic, Plastic plastic)
            {
                this.name = name;
                this.category = category;
                this.type = type;
                this.mass_density = mass_density;
                this.elastic = elastic;
                this.plastic = plastic;
            }
        }

        public class Elastic
        {
            public string behaviour_type;
            public ElasticParam parameters;

            public Elastic(string behaviour_type, ElasticParam parameters)
            {
                this.behaviour_type = behaviour_type;
                this.parameters = parameters;
            }
        }

        public class ElasticParam
        {
            public double E;
            public double v;

            public ElasticParam(double E, double v)
            {
                this.E = E;
                this.v = v;
            }
        }

        public class Plastic
        {
            public double? yield_stress;
            public double? plastic_strain;
            public object functions;

            public Plastic(double? yield_stress, double? plastic_strain, object functions)
            {
                this.yield_stress = yield_stress;
                this.plastic_strain = plastic_strain;
                this.functions = functions;
            }
        }

        public abstract class Section
        {
            public string id;
            public string name;
            public string section_type;
            public string material;

            protected Section(string id, string name, string section_type, string material)
            {
                this.id = id;
                this.name = name;
                this.section_type = section_type;
                this.material = material;
            }
        }

        public class BeamSection : Section
        {
            public string beam_section;
            public List<double> orientation;
            public CrossSectionProfile cross_section;

            public BeamSection(string id, string name, string material, string beam_section, List<double> orientation, CrossSectionProfile cross_section)
                : base(id, name, "BEAM SECTION", material)
            {
                this.beam_section = beam_section;
                this.orientation = orientation;
                this.cross_section = cross_section;
            }
        }

        public class ShellSection : Section
        {
            public double thickness;

            public ShellSection(string id, string name, string material, double thickness)
                : base(id, name, "SHELL SECTION", material)
            {
                this.thickness = thickness;
            }
        }

        // No parametric fields: geometry comes from the mesh/analysis itself. Added
        // for schema completeness (osam.py's SolidSection) - no Structure.cs
        // component creates a volumetric IFC structural member, so neither converter
        // produces or consumes this; it's a recognized, intentional no-op case.
        public class SolidSection : Section
        {
            public SolidSection(string id, string name, string material)
                : base(id, name, "SOLID SECTION", material)
            {
            }
        }

        public class Node
        {
            public double X;
            public double Y;
            public double Z;
            public int id;

            public Node(double X, double Y, double Z, int id)
            {
                this.X = X;
                this.Y = Y;
                this.Z = Z;
                this.id = id;

            }
        }

        public class Element
        {
            public int id;
            public string type;
            public List<int> dofs;
            public int node_count;
            public int face_count;
            public string integration;
            public List<int> nodes;
            public List<List<int>> faces;
            public string section;
            public string material;

            public Element(int id, string type, List<int> dofs, int node_count, int face_count, string integration, List<int> nodes,
                            List<List<int>> faces, string section, string material)
            {
                this.id = id;
                this.type = type;
                this.dofs = dofs;
                this.node_count = node_count;
                this.face_count = face_count;
                this.integration = integration;
                this.nodes = nodes;
                this.faces = faces;
                this.section = section;
                this.material = material;
            }
        }

        public class BoundaryCondition
        {
            public string id;
            public string type;
            public string nset;
            public List<string> instances;
            public List<object> ux;
            public List<object> uy;
            public List<object> uz;
            public List<object> rx;
            public List<object> ry;
            public List<object> rz;

            public BoundaryCondition(string id, string type, string nset, List<string> instances, List<object> ux, List<object> uy, List<object> uz,
                List<object> rx, List<object> ry, List<object> rz)
            {
                this.id = id;
                this.type = type;
                this.nset = nset;
                this.instances = instances;
                this.ux = ux;
                this.uy = uy;
                this.uz = uz;
                this.rx = rx;
                this.ry = ry;
                this.rz = rz;
            }
        }

        public class Nsets
        {
            public string name;
            public List<int> nodeIDs;

            public Nsets(string name, List<int> nodeIDs)
            {
                this.name = name;
                this.nodeIDs = nodeIDs;
            }
        }

        public class Elsets
        {
            public string name;
            public List<int> elementIDs;

            public Elsets(string name, List<int> elementIDs)
            {
                this.name = name;
                this.elementIDs = elementIDs;
            }
        }

        public class LoadCase
        {
            public string id;
            public string name;
            public string type;
            public List<double> selfWeight;

            public LoadCase(string id, string name, string type, List<double> selfWeight)
            {
                this.id = id;
                this.name = name;
                this.type = type;
                this.selfWeight = selfWeight;
            }
        }

        public abstract class Load
        {
            public string id;
            public string type;
            public string caseName;
            public List<string> instances;

            protected Load(string id, string type, string caseName, List<string> instances)
            {
                this.id = id;
                this.type = type;
                this.caseName = caseName;
                this.instances = instances;
            }
        }

        public class PointLoad : Load
        {
            public string nset;
            public int dof;
            public double v;

            public PointLoad(string id, string caseName, List<string> instances, string nset, int dof, double v)
                : base(id, "POINT_LOAD", caseName, instances)
            {
                this.nset = nset;
                this.dof = dof;
                this.v = v;
            }
        }

        public class DistributedLoad : Load
        {
            public string elset;
            public string dir;
            public double v1;
            public double v2;
            public double x1;
            public double x2;

            public DistributedLoad(string id, string caseName, List<string> instances, string elset, string dir, double v1, double v2, double x1, double x2)
                : base(id, "DISTRIBUTED_LOAD", caseName, instances)
            {
                this.elset = elset;
                this.dir = dir;
                this.v1 = v1;
                this.v2 = v2;
                this.x1 = x1;
                this.x2 = x2;
            }
        }

        public class SurfaceLoad : Load
        {
            public string elset;
            public double v;
            public double xdir;
            public double ydir;
            public double zdir;

            public SurfaceLoad(string id, string caseName, List<string> instances, string elset, double v, double xdir, double ydir, double zdir)
                : base(id, "SURFACE_LOAD", caseName, instances)
            {
                this.elset = elset;
                this.v = v;
                this.xdir = xdir;
                this.ydir = ydir;
                this.zdir = zdir;
            }
        }

        //Parametric cross sections
        public abstract class CrossSectionProfile
        {

        }

        public class RectProfile : CrossSectionProfile
        {
            public double a;
            public double b;

            public RectProfile(double a, double b)
            {
                this.a = a;
                this.b = b;
            }
        }

        public class IProfile : CrossSectionProfile
        {
            public double h;
            public double b1;
            public double b2;
            public double t1;
            public double t2;
            public double t3;
            // Optional Abaqus-only flange-offset parameter (7-value INP form).
            public double? l;

            public IProfile(double h, double b1, double b2, double t1, double t2, double t3, double? l = null)
            {
                this.h = h;
                this.b1 = b1;
                this.b2 = b2;
                this.t1 = t1;
                this.t2 = t2;
                this.t3 = t3;
                this.l = l;
            }
        }

        public class CircProfile : CrossSectionProfile
        {
            public double radius;

            public CircProfile(double radius)
            {
                this.radius = radius;
            }
        }

        public class LProfile : CrossSectionProfile
        {
            public double a;
            public double b;
            public double t1;
            public double t2;

            public LProfile(double a, double b, double t1, double t2)
            {
                this.a = a;
                this.b = b;
                this.t1 = t1;
                this.t2 = t2;
            }
        }

        public class BoxProfile : CrossSectionProfile
        {
            public double a;
            public double b;
            public double t1;
            public double t2;
            public double t3;
            public double t4;

            public BoxProfile(double a, double b, double t1, double t2, double t3, double t4)
            {
                this.a = a;
                this.b = b;
                this.t1 = t1;
                this.t2 = t2;
                this.t3 = t3;
                this.t4 = t4;
            }
        }

        public class PipeProfile : CrossSectionProfile
        {
            public double r;
            public double t;


            public PipeProfile(double r, double t)
            {
                this.r = r;
                this.t = t;
            }
        }


        public class ArbitraryProfile : CrossSectionProfile
        {
            public List<List<double>> edge_points;
            public List<List<List<double>>> void_points;

            public ArbitraryProfile(List<List<double>> edge_points, List<List<List<double>>> void_points)
            {
                this.edge_points = edge_points;
                this.void_points = void_points;
            }
        }

        // The following three are INP-only (HexProfile, TrapezoidProfile) or have no
        // IFC parametric-profile equivalent at all (GeneralProfile: direct area/inertia
        // values) - added for schema completeness with osam.py's HexProfile/
        // TrapezoidProfile/GeneralProfile, but neither converter produces or consumes
        // them since there is no IFC entity to round-trip them against.

        public class HexProfile : CrossSectionProfile
        {
            public double circ_r;
            public double t;

            public HexProfile(double circ_r, double t)
            {
                this.circ_r = circ_r;
                this.t = t;
            }
        }

        public class TrapezoidProfile : CrossSectionProfile
        {
            public double a;
            public double b;
            public double c;
            public double d;

            public TrapezoidProfile(double a, double b, double c, double d)
            {
                this.a = a;
                this.b = b;
                this.c = c;
                this.d = d;
            }
        }

        public class GeneralProfile : CrossSectionProfile
        {
            public double A;
            public double I11;
            public double I12;
            public double I22;
            public double J;

            public GeneralProfile(double A, double I11, double I12, double I22, double J)
            {
                this.A = A;
                this.I11 = I11;
                this.I12 = I12;
                this.I22 = I22;
                this.J = J;
            }
        }
    }

    // O-SAM -> Abaqus INP converter. Faithful port of osam_platform_backend's
    // osam_to_inp.py (app\converters\inp\osam_to_inp.py) - same card formats, unit
    // conversions, defaults, and known quirks/gaps (see method comments), operating
    // on the o_sam model above instead of the Pydantic StructuralAnalysisModel. Grouped under this
    // single class per request, including the JSON converters this conversion needs
    // to deserialize a .osam file into typed o_sam classes (o_sam itself carries no
    // serialization attributes, so these are registered via JsonSerializerSettings).
    public static class INP
    {
        // ── JSON converters (Section / Load / CrossSectionProfile are discriminated-
        // union types decided by a sibling field within the same flat JSON object,
        // with no built-in Newtonsoft wiring) ──────────────────────────────────────

        private class SectionConverter : JsonConverter
        {
            public override bool CanConvert(Type objectType) => objectType == typeof(o_sam.Section);
            public override bool CanWrite => false;

            public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
            {
                if (reader.TokenType == JsonToken.Null) return null;
                var obj = JObject.Load(reader);
                string id = (string)obj["id"];
                string name = (string)obj["name"];
                string sectionType = (string)obj["section_type"];
                string material = (string)obj["material"];

                switch (sectionType)
                {
                    case "BEAM SECTION":
                        {
                            string beamSection = (string)obj["beam_section"];
                            List<double> orientation = obj["orientation"]?.ToObject<List<double>>(serializer);
                            o_sam.CrossSectionProfile crossSection = obj["cross_section"]?.ToObject<o_sam.CrossSectionProfile>(serializer);
                            return new o_sam.BeamSection(id, name, material, beamSection, orientation, crossSection);
                        }
                    case "SHELL SECTION":
                        {
                            double thickness = obj["thickness"] != null ? (double)obj["thickness"] : 0.0;
                            return new o_sam.ShellSection(id, name, material, thickness);
                        }
                    case "SOLID SECTION":
                        return new o_sam.SolidSection(id, name, material);
                    default:
                        return null;
                }
            }

            public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
                => throw new NotSupportedException("SectionConverter is read-only.");
        }

        private class CrossSectionProfileConverter : JsonConverter
        {
            public override bool CanConvert(Type objectType) => objectType == typeof(o_sam.CrossSectionProfile);
            public override bool CanWrite => false;

            public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
            {
                if (reader.TokenType == JsonToken.Null) return null;
                var obj = JObject.Load(reader);
                string type = (string)obj["type"];
                switch (type)
                {
                    case "RECT": return obj.ToObject<o_sam.RectProfile>(serializer);
                    case "BOX": return obj.ToObject<o_sam.BoxProfile>(serializer);
                    case "PIPE": return obj.ToObject<o_sam.PipeProfile>(serializer);
                    case "CIRC": return obj.ToObject<o_sam.CircProfile>(serializer);
                    case "I": return obj.ToObject<o_sam.IProfile>(serializer);
                    case "L": return obj.ToObject<o_sam.LProfile>(serializer);
                    case "HEX": return obj.ToObject<o_sam.HexProfile>(serializer);
                    case "TRAPEZOID": return obj.ToObject<o_sam.TrapezoidProfile>(serializer);
                    case "GENERAL":
                    case "NON LINEAR GENERAL":
                        return obj.ToObject<o_sam.GeneralProfile>(serializer);
                    case "ARBITRARY": return obj.ToObject<o_sam.ArbitraryProfile>(serializer);
                    default: return null;
                }
            }

            public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
                => throw new NotSupportedException("CrossSectionProfileConverter is read-only.");
        }

        private class LoadConverter : JsonConverter
        {
            public override bool CanConvert(Type objectType) => objectType == typeof(o_sam.Load);
            public override bool CanWrite => false;

            public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
            {
                if (reader.TokenType == JsonToken.Null) return null;
                var obj = JObject.Load(reader);
                string id = (string)obj["id"];
                string type = (string)obj["type"];
                string caseName = (string)obj["caseName"];
                List<string> instances = obj["instances"]?.ToObject<List<string>>(serializer);

                switch (type)
                {
                    case "POINT_LOAD":
                        {
                            string nset = (string)obj["nset"];
                            int dof = obj["dof"] != null ? (int)obj["dof"] : 0;
                            double v = obj["v"] != null ? (double)obj["v"] : 0.0;
                            return new o_sam.PointLoad(id, caseName, instances, nset, dof, v);
                        }
                    case "DISTRIBUTED_LOAD":
                        {
                            string elset = (string)obj["elset"];
                            string dir = (string)obj["dir"];
                            double v1 = obj["v1"] != null ? (double)obj["v1"] : 0.0;
                            double v2 = obj["v2"] != null ? (double)obj["v2"] : 0.0;
                            double x1 = obj["x1"] != null ? (double)obj["x1"] : 0.0;
                            double x2 = obj["x2"] != null ? (double)obj["x2"] : 0.0;
                            return new o_sam.DistributedLoad(id, caseName, instances, elset, dir, v1, v2, x1, x2);
                        }
                    case "SURFACE_LOAD":
                        {
                            string elset = (string)obj["elset"];
                            double v = obj["v"] != null ? (double)obj["v"] : 0.0;
                            double xdir = obj["xdir"] != null ? (double)obj["xdir"] : 0.0;
                            double ydir = obj["ydir"] != null ? (double)obj["ydir"] : 0.0;
                            double zdir = obj["zdir"] != null ? (double)obj["zdir"] : 0.0;
                            return new o_sam.SurfaceLoad(id, caseName, instances, elset, v, xdir, ydir, zdir);
                        }
                    default:
                        return null;
                }
            }

            public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
                => throw new NotSupportedException("LoadConverter is read-only.");
        }

        /// <summary>
        /// JsonSerializerSettings pre-configured to deserialize a .osam file's JSON
        /// text into a typed o_sam.StructuralAnalysisModel graph (registers the three converters above).
        /// </summary>
        public static JsonSerializerSettings CreateSerializerSettings()
        {
            return new JsonSerializerSettings
            {
                Converters = new List<JsonConverter>
                {
                    new SectionConverter(),
                    new CrossSectionProfileConverter(),
                    new LoadConverter()
                }
            };
        }

        // ── Numeric formatting helpers (invariant culture throughout - Abaqus requires
        // period decimal separators regardless of the host machine's locale) ──────────

        private static string FormatG(double value, int sigDigits)
        {
            // .NET's "G<n>" is the closest equivalent to Python's "%.<n>g" (general
            // format, n significant digits, switches to scientific notation for very
            // large/small magnitudes) - only the exponent marker case differs.
            return value.ToString("G" + sigDigits, CultureInfo.InvariantCulture).Replace("E", "e");
        }

        private static string PadG(double value, int sigDigits, int width)
        {
            return FormatG(value, sigDigits).PadLeft(width);
        }

        private static string Inv(double value) => value.ToString(CultureInfo.InvariantCulture);

        // ── Names ───────────────────────────────────────────────────────────────────

        /// <summary>Port of _abaqus_name: '.'->'_' (Abaqus names can't contain periods),
        /// and prefixes "A_" if the name starts with a digit (Abaqus names can't start
        /// with a digit).</summary>
        public static string AbaqusName(string name)
        {
            if (string.IsNullOrEmpty(name)) return name ?? "";
            string result = name.Replace(".", "_");
            if (result.Length > 0 && char.IsDigit(result[0])) result = "A_" + result;
            return result;
        }

        // ── Elements ────────────────────────────────────────────────────────────────

        /// <summary>Port of _abaqus_element_type. face_count is never consulted; BEAM
        /// always maps to B31 (no B32); unmapped (type, integration, node_count)
        /// combinations return "" and the element is dropped by WriteElements.</summary>
        public static string AbaqusElementType(o_sam.Element el)
        {
            string t = el.type, intg = el.integration;
            int nc = el.node_count;
            if (t == "SHELL")
            {
                if (intg == "FULL" && nc == 4) return "S4";
                if (intg == "REDUCED" && nc == 4) return "S4R";
                if (intg == "FULL" && nc == 3) return "S3";
                if (intg == "REDUCED" && nc == 3) return "S3R";
                if (intg == "REDUCED" && nc == 8) return "S8R";
            }
            else if (t == "SOLID")
            {
                if (intg == "FULL" && nc == 4) return "C3D4";
                if (intg == "FULL" && nc == 8) return "C3D8";
                if (intg == "REDUCED" && nc == 8) return "C3D8R";
            }
            else if (t == "BEAM")
            {
                return "B31";
            }
            return "";
        }

        /// <summary>Port of _write_nodes: *NODE, coordinates m->mm, {: &gt;12.6g} each.</summary>
        public static string WriteNodes(List<o_sam.Node> nodes)
        {
            var lines = new List<string> { "*NODE" };
            foreach (var n in nodes)
            {
                lines.Add($"{n.id},{PadG(n.X * 1000, 6, 12)},{PadG(n.Y * 1000, 6, 12)},{PadG(n.Z * 1000, 6, 12)}");
            }
            return string.Join("\n", lines) + "\n\n";
        }

        /// <summary>Port of _write_elements: buckets elements by computed Abaqus type
        /// tag (insertion order preserved), one "*ELEMENT,  TYPE=..." block per tag
        /// (note the double space, reproduced exactly). Elements with no resolvable
        /// type tag are silently dropped, matching the reference.</summary>
        public static string WriteElements(List<o_sam.Element> elements)
        {
            var order = new List<string>();
            var buckets = new Dictionary<string, List<string>>();
            foreach (var el in elements)
            {
                string tag = AbaqusElementType(el);
                if (string.IsNullOrEmpty(tag)) continue;
                string header = $"*ELEMENT,  TYPE={tag}";
                if (!buckets.TryGetValue(header, out var rows))
                {
                    rows = new List<string>();
                    buckets[header] = rows;
                    order.Add(header);
                }
                string nodesStr = string.Join(",", el.nodes.Select(n => n.ToString(CultureInfo.InvariantCulture).PadLeft(8)));
                rows.Add($"{el.id},{nodesStr}");
            }
            if (order.Count == 0) return "";
            var parts = order.Select(header => header + "\n" + string.Join("\n", buckets[header]));
            return string.Join("\n\n", parts) + "\n\n";
        }

        // ── Sets ────────────────────────────────────────────────────────────────────

        private const int SetChunkSize = 16;

        private static string WriteIdSet(string header, List<int> ids)
        {
            var lines = new List<string> { header };
            var sorted = ids.OrderBy(x => x).ToList();
            for (int i = 0; i < sorted.Count; i += SetChunkSize)
            {
                var chunk = sorted.Skip(i).Take(SetChunkSize).ToList();
                string row = string.Join(", ", chunk.Select(n => n.ToString(CultureInfo.InvariantCulture).PadLeft(4)));
                if (chunk.Count == 1) row += ",";
                lines.Add(row);
            }
            return string.Join("\n", lines) + "\n";
        }

        /// <summary>Port of _write_nset: ids sorted, chunked 16/row, width-4 right-justified.</summary>
        public static string WriteNset(o_sam.Nsets nset, string instance = null)
        {
            string instStr = !string.IsNullOrEmpty(instance) ? $", instance={instance}" : "";
            return WriteIdSet($"*NSET, NSET={nset.name}{instStr}", nset.nodeIDs);
        }

        /// <summary>Port of _write_elset: byte-for-byte identical logic to WriteNset.</summary>
        public static string WriteElset(o_sam.Elsets elset, string instance = null)
        {
            string instStr = !string.IsNullOrEmpty(instance) ? $", instance={instance}" : "";
            return WriteIdSet($"*ELSET, ELSET={elset.name}{instStr}", elset.elementIDs);
        }

        // ── Beam orientation ────────────────────────────────────────────────────────

        private static readonly (double, double, double) DefaultBeamOrientation = (0.0, 0.0, -1.0);

        /// <summary>Port of _beam_orientation: a purely geometric local-N1 direction
        /// derived from the element's own first two node coordinates
        /// (StructuralObject.coordinateSystem is never consulted, matching the
        /// reference). Guards against &lt;2 nodes / unresolved node ids in addition to
        /// the reference's own degenerate-length guard - a defensive superset, not a
        /// behavior change for well-formed input (which never hits those extra
        /// guards).</summary>
        public static (double, double, double) BeamOrientation(o_sam.Element el, Dictionary<int, o_sam.Node> nodeById)
        {
            if (el.nodes == null || el.nodes.Count < 2) return DefaultBeamOrientation;
            if (!nodeById.TryGetValue(el.nodes[0], out var n1) || !nodeById.TryGetValue(el.nodes[1], out var n2))
                return DefaultBeamOrientation;

            double dx = n2.X - n1.X, dy = n2.Y - n1.Y, dz = n2.Z - n1.Z;
            double length = Math.Sqrt(dx * dx + dy * dy + dz * dz);
            if (length < 1e-10) return DefaultBeamOrientation;

            dx /= length; dy /= length; dz /= length;

            if (Math.Abs(dx) > 0.9999) return (0.0, dx > 0 ? 1.0 : -1.0, 0.0);
            if (Math.Abs(dy) > 0.9999) return (dy > 0 ? -1.0 : 1.0, 0.0, 0.0);
            if (Math.Abs(dz) > 0.9999) return (dz > 0 ? 1.0 : -1.0, 0.0, 0.0);
            if (Math.Abs(dz) < 1e-6) return (0.0, 0.0, 1.0);
            if (Math.Abs(dx) < 1e-6) return (dy > 0 ? -1.0 : 1.0, 0.0, 0.0);
            if (Math.Abs(dy) < 1e-6) return (0.0, dx > 0 ? 1.0 : -1.0, 0.0);

            double n1x = -dy, n1y = dx;
            double n1Len = Math.Sqrt(n1x * n1x + n1y * n1y);
            if (n1Len > 1e-10) return (Math.Round(n1x / n1Len, 10), Math.Round(n1y / n1Len, 10), 0.0);
            return (1.0, 0.0, 0.0);
        }

        // ── Sections ────────────────────────────────────────────────────────────────

        /// <summary>Port of the reference's beam cross-section -> Abaqus geometry-data-
        /// line mapping (all values already ×1000/×1e6/×1e12 as applicable). CIRC
        /// deliberately never reads CircProfile.radius: the reference reads
        /// cross_section["r"], but osam.py's CircProfile field is "radius", so that key
        /// is always absent in real data and the reference always falls back to its
        /// 0.1 default - reproduced exactly by simply not reading the real value. RECT
        /// emits (b, a) - reversed relative to the schema's a,b naming, exactly as the
        /// reference does.</summary>
        private static List<double> BuildBeamGeomArgs(string sType, o_sam.CrossSectionProfile cs)
        {
            switch (sType)
            {
                case "BOX":
                    {
                        var s = cs as o_sam.BoxProfile;
                        double a = s?.a ?? 0.1, b = s?.b ?? 0.1, t1 = s?.t1 ?? 0.01, t2 = s?.t2 ?? 0.01, t3 = s?.t3 ?? 0.01, t4 = s?.t4 ?? 0.01;
                        return new List<double> { a * 1000, b * 1000, t1 * 1000, t2 * 1000, t3 * 1000, t4 * 1000 };
                    }
                case "CIRC":
                    return new List<double> { 0.1 * 1000 };
                case "HEX":
                    {
                        var s = cs as o_sam.HexProfile;
                        double circR = s?.circ_r ?? 0.1, t = s?.t ?? 0.01;
                        return new List<double> { circR * 1000, t * 1000 };
                    }
                case "I":
                    {
                        var s = cs as o_sam.IProfile;
                        double l = s?.l ?? 0.2, h = s?.h ?? 0.4, b1 = s?.b1 ?? 0.2, b2 = s?.b2 ?? 0.2;
                        double t1 = s?.t1 ?? 0.02, t2 = s?.t2 ?? 0.02, t3 = s?.t3 ?? 0.02;
                        return new List<double> { l * 1000, h * 1000, b1 * 1000, b2 * 1000, t1 * 1000, t2 * 1000, t3 * 1000 };
                    }
                case "L":
                    {
                        var s = cs as o_sam.LProfile;
                        double a = s?.a ?? 0.1, b = s?.b ?? 0.1, t1 = s?.t1 ?? 0.01, t2 = s?.t2 ?? 0.01;
                        return new List<double> { a * 1000, b * 1000, t1 * 1000, t2 * 1000 };
                    }
                case "PIPE":
                    {
                        var s = cs as o_sam.PipeProfile;
                        double r = s?.r ?? 0.1, t = s?.t ?? 0.01;
                        return new List<double> { r * 1000, t * 1000 };
                    }
                case "RECT":
                    {
                        var s = cs as o_sam.RectProfile;
                        double a = s?.a ?? 0.1, b = s?.b ?? 0.1;
                        return new List<double> { b * 1000, a * 1000 };
                    }
                case "TRAPEZOID":
                    {
                        var s = cs as o_sam.TrapezoidProfile;
                        double a = s?.a ?? 0.1, b = s?.b ?? 0.1, c = s?.c ?? 0.1, d = s?.d ?? 0.0;
                        return new List<double> { a * 1000, b * 1000, c * 1000, d * 1000 };
                    }
                case "GENERAL":
                case "NON LINEAR GENERAL":
                    {
                        var s = cs as o_sam.GeneralProfile;
                        double A = s?.A ?? 0.0, I11 = s?.I11 ?? 0.0, I12 = s?.I12 ?? 0.0, I22 = s?.I22 ?? 0.0, J = s?.J ?? 0.0;
                        return new List<double> { A * 1e6, I11 * 1e12, I12 * 1e12, I22 * 1e12, J * 1e12 };
                    }
                default:
                    return new List<double>();
            }
        }

        /// <summary>Port of _write_sections. Elements are grouped by (section id,
        /// effective material, beam-orientation-or-null) - beams sharing a section and
        /// material but pointing different directions get separate elset+section
        /// blocks. An element whose section doesn't resolve to any Section.id is
        /// silently skipped (still appears in *NODE/*ELEMENT, gets no section
        /// card).</summary>
        public static string WriteSections(List<o_sam.Section> allSections, o_sam.StructuralObject obj)
        {
            var nodeById = obj.mesh.nodes.ToDictionary(n => n.id, n => n);
            var sectionsById = allSections.ToDictionary(s => s.id, s => s);

            var order = new List<(string sectionId, string material, (double, double, double)? orient)>();
            var groups = new Dictionary<(string, string, (double, double, double)?), List<int>>();

            foreach (var el in obj.mesh.elements)
            {
                if (!sectionsById.TryGetValue(el.section, out var sec) || sec == null) continue;

                string matId = el.material;
                (double, double, double)? orient = null;
                if (AbaqusElementType(el).StartsWith("B"))
                {
                    orient = BeamOrientation(el, nodeById);
                }

                var key = (el.section, matId, orient);
                if (!groups.TryGetValue(key, out var list))
                {
                    list = new List<int>();
                    groups[key] = list;
                    order.Add(key);
                }
                list.Add(el.id);
            }

            var lines = new List<string>();
            int setNum = 0;
            foreach (var key in order)
            {
                var (secId, matId, elemOrient) = key;
                var elIds = groups[key];
                var sec = sectionsById[secId];
                string elsetName = $"set{setNum}";
                setNum++;
                lines.Add(WriteElset(new o_sam.Elsets(elsetName, elIds)));

                string actualMat = !string.IsNullOrEmpty(matId) ? matId : sec.material;
                string matName = AbaqusName(actualMat);

                if (sec is o_sam.ShellSection shellSection)
                {
                    double thicknessMm = shellSection.thickness * 1000;
                    lines.Add($"*Shell Section, ELSET={elsetName}, MATERIAL={matName}\n{Inv(thicknessMm)}\n");
                }
                else if (sec is o_sam.SolidSection)
                {
                    lines.Add($"*SOLID SECTION, ELSET={elsetName}, MATERIAL={matName}\n");
                }
                else if (sec is o_sam.BeamSection beamSection)
                {
                    string secName = AbaqusName(sec.name);
                    string compName = (!string.IsNullOrEmpty(matId) && matId != sec.material) ? $"{secName}_{matName}" : secName;
                    string sType = !string.IsNullOrEmpty(beamSection.beam_section) ? beamSection.beam_section : "RECT";

                    lines.Add($"** Section: {compName}  Profile: {compName}");
                    lines.Add($"*Beam General Section, elset={elsetName}, material={matName}, section={sType}");

                    var geomArgs = BuildBeamGeomArgs(sType, beamSection.cross_section);
                    if (geomArgs.Count > 0)
                    {
                        lines.Add(string.Join(", ", geomArgs.Select(Inv)));
                    }
                    else if (sType != "ARBITRARY")
                    {
                        lines.Add("0.1, 0.1");
                    }

                    if (elemOrient.HasValue)
                    {
                        var (ox, oy, oz) = elemOrient.Value;
                        lines.Add($"{Inv(ox)}, {Inv(oy)}, {Inv(oz)}");
                    }
                    else if (beamSection.orientation != null && beamSection.orientation.Count >= 3)
                    {
                        lines.Add($"{Inv(beamSection.orientation[0])}, {Inv(beamSection.orientation[1])}, {Inv(beamSection.orientation[2])}");
                    }
                    else
                    {
                        lines.Add("0., 0., -1.");
                    }
                    lines.Add("");
                }
            }

            return string.Join("\n", lines);
        }

        // ── Parts / Instances / Assembly ────────────────────────────────────────────

        /// <summary>Port of _write_part: *Part/*End Part wrapping *NODE, *ELEMENT and
        /// section blocks for one StructuralObject.</summary>
        public static string WritePart(o_sam.StructuralObject obj, List<o_sam.Section> allSections)
        {
            string name = AbaqusName(obj.name);
            var lines = new List<string> { $"*Part, name={name}", "" };
            lines.Add(WriteNodes(obj.mesh.nodes));
            lines.Add(WriteElements(obj.mesh.elements));
            lines.Add(WriteSections(allSections, obj));
            lines.Add("*End Part\n");
            return string.Join("\n", lines);
        }

        /// <summary>Resolves an Instance's Abaqus name, appending "-1" if it would
        /// otherwise collide with its Part's name (Abaqus disallows that) - shared by
        /// WriteInstance and WriteAssembly so the same value is computed once, unlike
        /// the reference which recomputes this inline in both places.</summary>
        private static string ResolveInstanceName(o_sam.Instance inst, List<o_sam.StructuralObject> objects)
        {
            var obj = objects.FirstOrDefault(o => o.id == inst.referenced_object);
            string instName = AbaqusName(inst.name);
            string objName = AbaqusName(obj != null ? obj.name : inst.name);
            return instName == objName ? instName + "-1" : instName;
        }

        /// <summary>Port of _write_instance: *INSTANCE/*END INSTANCE with optional
        /// translation (NOT unit-scaled, unlike node coordinates - reproduced exactly)
        /// and rotation (point A, point B, angle) data lines.</summary>
        public static string WriteInstance(o_sam.Instance inst, List<o_sam.StructuralObject> objects)
        {
            var obj = objects.FirstOrDefault(o => o.id == inst.referenced_object);
            string objName = AbaqusName(obj != null ? obj.name : inst.name);
            string instName = ResolveInstanceName(inst, objects);

            var lines = new List<string> { $"*INSTANCE, NAME={instName}, PART={objName}" };

            if (inst.translation != null)
            {
                var t = inst.translation;
                lines.Add($"{Inv(t.X)},{Inv(t.Y).PadLeft(4)},{Inv(t.Z).PadLeft(4)}");
            }
            if (inst.rotation != null)
            {
                var r = inst.rotation;
                double ax = r.A?.X ?? 0.0, ay = r.A?.Y ?? 0.0, az = r.A?.Z ?? 0.0;
                double bx = r.B?.X ?? 0.0, by = r.B?.Y ?? 0.0, bz = r.B?.Z ?? 1.0;
                lines.Add($"{Inv(ax)},{Inv(ay).PadLeft(8)},{Inv(az).PadLeft(8)},{Inv(bx).PadLeft(8)},{Inv(by).PadLeft(8)},{Inv(bz).PadLeft(8)},{Inv(r.angle).PadLeft(8)}");
            }
            lines.Add("");
            lines.Add("*END INSTANCE\n");
            return string.Join("\n", lines);
        }

        /// <summary>Port of _write_assembly: all *Part blocks, then *ASSEMBLY with every
        /// *INSTANCE, each instance's *NSET/*ELSET (instance-qualified), one
        /// *Surface/SPOS per unique elset referenced by a SurfaceLoad, then
        /// *END ASSEMBLY.</summary>
        public static string WriteAssembly(o_sam.Assembly assembly, List<o_sam.StructuralObject> objects,
            List<o_sam.Section> allSections, List<o_sam.Load> loads)
        {
            var parts = new List<string>();
            foreach (var obj in objects)
            {
                parts.Add(WritePart(obj, allSections));
            }

            string asmName = AbaqusName(assembly.name);
            parts.Add($"*ASSEMBLY, NAME={asmName}\n");

            foreach (var inst in assembly.instances)
            {
                parts.Add(WriteInstance(inst, objects));
            }

            foreach (var inst in assembly.instances)
            {
                string instName = ResolveInstanceName(inst, objects);
                if (inst.nsets != null)
                {
                    foreach (var nset in inst.nsets) parts.Add(WriteNset(nset, instName));
                }
                if (inst.elsets != null)
                {
                    foreach (var elset in inst.elsets) parts.Add(WriteElset(elset, instName));
                }
            }

            var recorded = new HashSet<string>();
            foreach (var load in loads)
            {
                if (load is o_sam.SurfaceLoad surfaceLoad && !recorded.Contains(surfaceLoad.elset))
                {
                    parts.Add($"*Surface, type=ELEMENT, name={surfaceLoad.elset}\n{surfaceLoad.elset}, SPOS\n");
                    recorded.Add(surfaceLoad.elset);
                }
            }

            parts.Add("\n*END ASSEMBLY\n");
            return string.Join("\n", parts);
        }

        // ── Materials ───────────────────────────────────────────────────────────────

        /// <summary>Port of _write_material: *Material always emitted; *Density only if
        /// mass_density&gt;0 (kg/m3->tonne/mm3); *Elastic only if E!=0 (no unit scaling -
        /// E/v assumed already in target units); *Plastic only if yield_stress is set
        /// (single point only, no multi-point hardening curve support).</summary>
        public static string WriteMaterial(o_sam.Material mat)
        {
            string name = AbaqusName(mat.name);
            var lines = new List<string> { $"*Material, name={name}" };

            if (mat.mass_density > 0)
            {
                double densityTonn = mat.mass_density * 1e-12;
                lines.Add($"*Density\n{FormatG(densityTonn, 12)},");
            }

            var parameters = mat.elastic?.parameters;
            if (parameters != null && parameters.E != 0)
            {
                string btype = (mat.elastic.behaviour_type ?? "ISOTROPIC").ToUpperInvariant();
                lines.Add(btype == "ISOTROPIC" ? "*Elastic" : $"*Elastic, type={btype}");
                lines.Add($"{Inv(parameters.E)}, {Inv(parameters.v)}");
            }

            if (mat.plastic != null && mat.plastic.yield_stress.HasValue)
            {
                lines.Add("*Plastic");
                lines.Add($"{Inv(mat.plastic.yield_stress.Value)}, {Inv(mat.plastic.plastic_strain ?? 0.0)}");
            }

            return string.Join("\n", lines);
        }

        // ── Boundary conditions ─────────────────────────────────────────────────────

        private static bool IsDofActive(List<object> vals)
        {
            if (vals == null || vals.Count == 0 || vals[0] == null) return false;
            if (vals[0] is bool b) return b;
            try { return Convert.ToDouble(vals[0], CultureInfo.InvariantCulture) != 0.0; }
            catch (InvalidCastException) { return false; }
            catch (FormatException) { return false; }
        }

        private static string BcLine(string nset, int dof, List<object> vals)
        {
            double mag = 0.0;
            if (vals != null && vals.Count > 1 && vals[1] != null)
            {
                try { mag = Convert.ToDouble(vals[1], CultureInfo.InvariantCulture); }
                catch (InvalidCastException) { mag = 0.0; }
                catch (FormatException) { mag = 0.0; }
            }
            return mag == 0.0 ? $"{nset}, {dof}, {dof}" : $"{nset}, {dof}, {dof}, {Inv(mag)}";
        }

        /// <summary>Port of _write_bcs. Each ux/uy/uz/rx/ry/rz list is read as
        /// [isActive, magnitude]; a DOF is emitted only if vals[0] is truthy. DOF
        /// numbers 1=Ux,2=Uy,3=Uz,4=Rx,5=Ry,6=Rz. Zero magnitude -&gt; 3-field (fixed);
        /// nonzero -&gt; 4-field (prescribed). BoundaryCondition.instances is never used
        /// (nset emitted unqualified), matching the reference.</summary>
        public static string WriteBcs(List<o_sam.BoundaryCondition> bcs)
        {
            var lines = new List<string>();
            int i = 0;
            foreach (var bc in bcs)
            {
                i++;
                bool[] active = { IsDofActive(bc.ux), IsDofActive(bc.uy), IsDofActive(bc.uz),
                                   IsDofActive(bc.rx), IsDofActive(bc.ry), IsDofActive(bc.rz) };
                if (!active.Any(a => a)) continue;

                lines.Add($"** Name: BC-{i} Type: Displacement/Rotation\n*Boundary");
                string nset = bc.nset;
                if (active[0]) lines.Add(BcLine(nset, 1, bc.ux));
                if (active[1]) lines.Add(BcLine(nset, 2, bc.uy));
                if (active[2]) lines.Add(BcLine(nset, 3, bc.uz));
                if (active[3]) lines.Add(BcLine(nset, 4, bc.rx));
                if (active[4]) lines.Add(BcLine(nset, 5, bc.ry));
                if (active[5]) lines.Add(BcLine(nset, 6, bc.rz));
            }
            return lines.Count > 0 ? string.Join("\n", lines) + "\n" : "";
        }

        // ── Loads / Steps ───────────────────────────────────────────────────────────

        /// <summary>Port of _write_loads_step. Loads are grouped by Load.caseName
        /// (default "DefaultLoadCase") - model.loadCases (incl. selfWeight) is never
        /// consulted, so self-weight/gravity is unimplemented, matching the reference.
        /// No loads at all -&gt; one hardcoded generic Step-1. DistributedLoad's v1/v2
        /// are averaged into a single uniform value; x1/x2 extents are discarded
        /// entirely (no linearly-varying line-load support), matching the
        /// reference.</summary>
        public static string WriteLoadsStep(List<o_sam.Load> loads)
        {
            var caseOrder = new List<string>();
            var casesByName = new Dictionary<string, List<o_sam.Load>>();
            foreach (var load in loads)
            {
                string cname = !string.IsNullOrEmpty(load.caseName) ? load.caseName : "DefaultLoadCase";
                if (!casesByName.TryGetValue(cname, out var list))
                {
                    list = new List<o_sam.Load>();
                    casesByName[cname] = list;
                    caseOrder.Add(cname);
                }
                list.Add(load);
            }

            if (caseOrder.Count == 0)
            {
                return "*Step, name=Step-1, nlgeom=NO, inc=5\n"
                     + "*Static, direct\n0.2, 1.,\n"
                     + "**\n** OUTPUT REQUESTS\n**\n"
                     + "*RESTART, WRITE, FREQUENCY=0\n"
                     + "*OUTPUT, FIELD, VARIABLE=PRESELECT\n"
                     + "*OUTPUT, HISTORY, VARIABLE=PRESELECT\n"
                     + "*END STEP\n";
            }

            var parts = new List<string>();
            int stepNum = 0;
            foreach (var cname in caseOrder)
            {
                stepNum++;
                parts.Add($"*Step, name=Step-{stepNum}, nlgeom=NO, inc=5");
                parts.Add("*Static, direct\n0.2, 1.,");
                parts.Add("**\n** LOADS\n**");

                foreach (var load in casesByName[cname])
                {
                    string lid = (load.id ?? "").Length > 8 ? load.id.Substring(0, 8) : (load.id ?? "");

                    if (load is o_sam.PointLoad nodal)
                    {
                        double vN = nodal.v * 1000.0;
                        parts.Add($"** \n** Name: Load-{lid}   Type: Concentrated force\n*CLOAD\n{nodal.nset}, {nodal.dof}, {Inv(vN)}");
                    }
                    else if (load is o_sam.SurfaceLoad surface)
                    {
                        bool hasDir = surface.xdir != 0 || surface.ydir != 0 || surface.zdir != 0;
                        parts.Add($"** \n** Name: Load-{lid}   Type: Pressure/Traction\n*DSLOAD");
                        parts.Add(hasDir
                            ? $"{surface.elset}, TRVEC, {Inv(surface.v)}, {Inv(surface.xdir)}, {Inv(surface.ydir)}, {Inv(surface.zdir)}"
                            : $"{surface.elset}, P, {Inv(surface.v)}");
                    }
                    else if (load is o_sam.DistributedLoad dist)
                    {
                        string fixedDir = (dist.dir ?? "").ToUpperInvariant().Replace("F", "P");
                        double avgV = (dist.v1 + dist.v2) / 2.0;
                        parts.Add($"** \n** Name: Load-{lid}   Type: Line load\n*DLOAD\n{dist.elset}, {fixedDir}, {Inv(avgV)}");
                    }
                }

                parts.Add("**\n** OUTPUT REQUESTS\n**");
                parts.Add("*RESTART, WRITE, FREQUENCY=0\n*OUTPUT, FIELD, VARIABLE=PRESELECT\n*OUTPUT, HISTORY, VARIABLE=PRESELECT");
                parts.Add("*END STEP\n");
            }

            return string.Join("\n", parts);
        }

        // ── Entry point ─────────────────────────────────────────────────────────────

        /// <summary>Port of osam_to_inp: the full Abaqus .inp text for the given
        /// model. Pure function - no file I/O (mirrors the reference's contract; the
        /// caller/component is responsible for writing the result to disk).</summary>
        public static string BuildInpText(o_sam.StructuralAnalysisModel model)
        {
            var pieces = new List<string>
            {
                "*Heading\n** Generated by OSAM INP Converter\n",
                WriteAssembly(model.assembly, model.objects, model.sections, model.loads)
            };

            if (model.materials != null && model.materials.Count > 0)
            {
                pieces.Add("**\n** MATERIALS\n**");
                foreach (var mat in model.materials)
                {
                    pieces.Add(WriteMaterial(mat));
                }
            }

            pieces.Add("**\n** BOUNDARY CONDITIONS\n**");
            pieces.Add(WriteBcs(model.bc ?? new List<o_sam.BoundaryCondition>()));

            pieces.Add(WriteLoadsStep(model.loads ?? new List<o_sam.Load>()));

            return string.Join("\n", pieces);
        }
    }
