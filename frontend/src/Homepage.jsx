export default function Homepage({ user, setUser }) {
  return (
    <>
      {user.success && (
        <div>
          <h2 className="login-title">Welcome {user.username}</h2>
          <button className="login-button" onClick={()=>(setUser((prev)=>({...prev, success:false})))}>
            Logout
          </button>
        </div>
      )}
    </>
  );
}
