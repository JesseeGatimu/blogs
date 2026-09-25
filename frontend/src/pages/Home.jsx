import Navbar from "../components/Navbar";
function Home(){
    return (
        <div>
            <Navbar/>
            <main>
                <section>
                    <p>Welcome to Blog .</p>
                    <h1>Ideas Worth
                        <br/>
                        Sharing
                    </h1>
                    <p>Discove rinteresting stories, news and 
                        perspectives from people all over 
                        the world.
                    </p>
                    <div>
                        <button>
                            Explore Posts
                        </button>
                        <button>
                            Write Posts
                        </button>
                    </div>
                </section>
            </main>
        </div>
    )
}
export default Home;