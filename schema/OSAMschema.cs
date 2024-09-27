public class o_sam
{

    public class O_SAM
    {
        public string id;
        public string name;
        public Units units;
        public List<objects> objects;
        public Assembly assembly;
        public List<Material> materials;
        public List<Section> sections;
        public List<BoundaryCondition> bc;
        public List<LoadCase> loadCases;
        public List<Load> loads;

        public O_SAM(string id, string name, Units units, List<objects> objects, Assembly assembly, List<Material> materials, List<Section> sections,
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

        public Units(string force, string length, string temperature, string time)
        {
            this.force = force;
            this.length = length;
            this.temperature = temperature;
            this.time = time;
        }
    }

    public class objects
    {
        public string id;
        public string name;
        public Mesh mesh;
        public CoordinateSystem coordinateSystem;

        public objects(string id, string name, Mesh mesh, CoordinateSystem coordinateSystem)
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

    public class Point3D
    {
        public double X;
        public double Y;
        public double Z;

        public Point3D(double X, double Y, double Z)
        {
            this.X = X;
            this.Y = Y;
            this.Z = Z;
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
        public List<nsets> nsets;
        public List<elsets> elsets;
        public List<object> translation;
        public List<object> rotation;

        public Instance(string id, string name, string referenced_object, List<nsets> nsets, List<elsets> elsets,
            List<object> translation, List<object> rotation)
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
        public object functions;
        public bool plane_stress;
        public bool plane_stain;
        public double compression_factor;
        public ElasticParam parameters;

        public Elastic(object functions, bool plane_stress, bool plane_strain, double compression_factor, ElasticParam parameters)
        {
            this.functions = functions;
            this.plane_stress = plane_stress;
            this.plane_stain = plane_strain;
            this.compression_factor = compression_factor;
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
        public object functions;

        public Plastic(object functions)
        {
            this.functions = functions;
        }
    }

    public class Section
    {
        public string id;
        public string name;
        public string section_type;
        public SectionType section;

        public Section(string id, string name, string section_type, SectionType section)
        {
            this.id = id;
            this.name = name;
            this.section_type = section_type;
            this.section = section;
        }
    }

    public abstract class SectionType
    {

    }

    public class BeamSection : SectionType
    {
        public string beam_section;
        public List<double> orientation;
        public CrossSection cross_section;

        public BeamSection(string beam_section, List<double> orientation, CrossSection cross_section)
        {
            this.beam_section = beam_section;
            this.orientation = orientation;
            this.cross_section = cross_section;
        }
    }

    public class ShellSection : SectionType
    {
        public double thickness;

        public ShellSection(double thickness)
        {
            this.thickness = thickness;
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
        public string nodes;
        public List<string> instances;
        public List<object> ux;
        public List<object> uy;
        public List<object> uz;
        public List<object> rx;
        public List<object> ry;
        public List<object> rz;

        public BoundaryCondition(string id, string type, string nodes, List<string> instances, List<object> ux, List<object> uy, List<object> uz,
            List<object> rx, List<object> ry, List<object> rz)
        {
            this.id = id;
            this.type = type;
            this.nodes = nodes;
            this.instances = instances;
            this.ux = ux;
            this.uy = uy;
            this.uz = uz;
            this.rx = rx;
            this.ry = ry;
            this.rz = rz;
        }
    }

    public class nsets
    {
        public string name;
        public List<int> nodesIDs;

        public nsets(string name, List<int> nodesIDs)
        {
            this.name = name;
            this.nodesIDs = nodesIDs;
        }
    }

    public class elsets
    {
        public string name;
        public List<int> elemsIDs;

        public elsets(string name, List<int> elemsIDs)
        {
            this.name = name;
            this.elemsIDs = elemsIDs;
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

    public class Load
    {
        public string id;
        public string type;
        public string caseName;
        public List<string> instances;
        public LoadType load;

        public Load(string id, string type, string caseName, List<string> instances, LoadType load)
        {
            this.id = id;
            this.type = type;
            this.caseName = caseName;
            this.instances = instances;
            this.load = load;
        }
    }

    public abstract class LoadType
    {

    }

    public class NodalLoad : LoadType
    {
        public string nset;
        public int dof;
        public double v;

        public NodalLoad(string nset, int dof, double v)
        {
            this.nset = nset;
            this.dof = dof;
            this.v = v;
        }
    }

    //Parametric cross sections
    public abstract class CrossSection
    {

    }

    public class RectSection : CrossSection
    {
        public double a;
        public double b;

        public RectSection(double a, double b)
        {
            this.a = a;
            this.b = b;
        }
    }

    public class ISection : CrossSection
    {
        public double h;
        public double b1;
        public double b2;
        public double t1;
        public double t2;
        public double t3;

        public ISection(double h, double b1, double b2, double t1, double t2, double t3)
        {
            this.h = h;
            this.b1 = b1;
            this.b2 = b2;
            this.t1 = t1;
            this.t2 = t2;
            this.t3 = t3;
        }
    }

    public class CircSection : CrossSection
    {
        public double radius;

        public CircSection(double radius)
        {
            this.radius = radius;
        }
    }

    public class LSection : CrossSection
    {
        public double a;
        public double b;
        public double t1;
        public double t2;

        public LSection(double a, double b, double t1, double t2)
        {
            this.a = a;
            this.b = b;
            this.t1 = t1;
            this.t2 = t2;
        }
    }

    public class BoxSection : CrossSection
    {
        public double a;
        public double b;
        public double t1;
        public double t2;
        public double t3;
        public double t4;

        public BoxSection(double a, double b, double t1, double t2, double t3, double t4)
        {
            this.a = a;
            this.b = b;
            this.t1 = t1;
            this.t2 = t2;
            this.t2 = t3;
            this.t4 = t4;
        }
    }

    public class PipeSection : CrossSection
    {
        public double r;
        public double t;


        public PipeSection(double r, double t)
        {
            this.r = r;
            this.t = t;
        }
    }


    public class ArbitrarySection : CrossSection
    {
        public List<List<double>> edge_points;
        public List<List<List<double>>> void_points;

        public ArbitrarySection(List<List<double>> edge_points, List<List<List<double>>> void_points)
        {
            this.edge_points = edge_points;
            this.void_points = void_points;
        }
    }
}
